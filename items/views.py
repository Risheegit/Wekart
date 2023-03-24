from django.shortcuts import render, HttpResponseRedirect
from .models import Item
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ItemListView (LoginRequiredMixin, ListView):
    login_url = '/login'
    paginate_by = 8
    model = Item
    template_name = 'items/home.html'
    context_object_name = 'items'

class ItemCreateView (LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Item
    fields = ['itemName', 'qty', 'tags', 'image', 'price']
    success_url = '/items'  

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

	# def test_func(self):
	# 	posts = self.get_object()
	# 	if self.request.user == posts.op_name :
	# 		return True
	# 	return False

class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        status = item.favorite
        print('status is ', status)
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