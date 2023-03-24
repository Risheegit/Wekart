from django.urls import path, reverse_lazy
from . import views
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView, AddLike, FavoriteDetailView, ItemSearch

urlpatterns = [
    path ('', ItemListView.as_view(), name ='home'),
    path ('new/', ItemCreateView.as_view(), name ='create'),
    path('favorite/', views.FavoriteDetailView, name = 'favorites'),
    path('search/', ItemSearch.as_view(), name='search'),
    path('<pk>/update/', ItemUpdateView.as_view(), name = 'update'),
    path ('<pk>/delete/', ItemDeleteView.as_view(), name ='delete'),
    path ('<pk>/like/', AddLike.as_view(), name ='like'),
]

