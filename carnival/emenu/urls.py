#create url for menu view
from django.urls import path
from . import views

app_name = 'emenu'
urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<int:id>', views.menu, name='menu_detail'),
]
