from django.urls import  path
from .views import ProductListView


urlpatterns = [
    path('product/' , ProductListView.as_view() , name= 'products')
    
]
