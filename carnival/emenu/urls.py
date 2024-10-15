#create url for menu view
from django.urls import path
from . import views

app_name = 'emenu'
urlpatterns = [
    path('', views.menu_list, name='vendors-list'),
    path('vendors', views.menu_list, name='vendors-list'),
    path('vendors/<int:id>', views.menu, name='vendor-detail'),
    path('gallery', views.gallery, name='gallery'),
    path('api/vendors-search', views.vendors_search, name='vendors-search'),
]
