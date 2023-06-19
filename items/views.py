from django.shortcuts import render, HttpResponseRedirect
from .models import Item
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib import messages

# Create your views here.
class ItemListView (ListView):
    login_url = '/login'
    paginate_by = 8
    model = Item
    # queryset = Item.objects.filter(shopkeeper = self.request.user)
    template_name = 'items/home.html'
    context_object_name = 'items'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            qs = super(ItemListView, self).get_queryset(*args, **kwargs)
            qs = qs.exclude(shopkeeper = self.request.user)
            qs = qs.filter(qty__gt=0)
            return qs
        else :
            qs = super(ItemListView, self).get_queryset(*args, **kwargs)
            return qs

class ItemCreateView (LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Item
    fields = ['itemName', 'qty', 'tags', 'image', 'price']
    success_url = '/items'  
    
    def form_valid(self, form):
        print('form valid is run')
        instance = form.save(commit=False)
        qty = form.cleaned_data['qty']
        print(qty)
        # if qty < 0:
        #     raise ValidationError('Qty must be positive')
        form.save()
        # messages.success(self.request, _("successful"))
        form.instance.shopkeeper = self.request.user
        return super().form_valid(form)


    # def clean_qty(self, form):
    #     print('clean_qty called')
    #     qty = form.cleaned_data['qty']
    #     if qty < 0:
    #         raise ValidationError('Quantity must be a positive number')
    #     return qty
    
    def form_valid(self, form):
        form.instance.shopkeeper = self.request.user
        # form.cleaned_data['qty'] = self.clean_qty()
        return super().form_valid(form)

def FavoriteDetailView (request):
    favorites = Item.objects.filter(favorite = True)
    context = {'items': favorites, 'showPages':False}
    return render(request, 'items/home.html', context)

class ItemUpdateView (LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Item
    fields = ['itemName', 'qty', 'image', 'tags', 'price']
    success_url = '/items'

class ItemDeleteView (LoginRequiredMixin, DeleteView):
	login_url = '/login'
	model = Item
	success_url = '/items'

	def test_func(self):
		items = self.get_object()
		if self.request.user == items.shopkeeper :
			return True
		return False

class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        status = item.favorite
        if status:
            item.favorite = False
        else: 
            item.favorite = True
        item.save()
        next = request.POST.get('next', '/items')
        return HttpResponseRedirect(next)

class ItemSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        items = Item.objects.filter(Q(tags__icontains=query) | Q(itemName__icontains=query))
        context = {
            'items': items,
        }
        return render(request, 'items/home.html', context)

class AddToCart(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk = pk)
        seller = item.shopkeeper
        item.cart.add(request.user)
        item.save()
        next = request.POST.get('next', '/items')
        return HttpResponseRedirect(next)

class BuyItem(LoginRequiredMixin, View):

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        max_value = item.qty
        context = {
            'item' : item,
            'max_value' : max_value
        }
        return render(request, 'items/item_buy.html', context)

    def post(self, request, pk, *args, **kwargs):
        qty = request.POST.get('quantity')
        item = Item.objects.get(pk = pk)
        item.qty = item.qty - int(qty)
        item.save()
        # return render(request, 'items/home.html')
        next = request.POST.get('next', '/items')
        return HttpResponseRedirect(next)