from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from  rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter



class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().distinct()
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        
        ]
    filterset_class  =  ProductFilter
    search_fields = ['name', 'description' , 'price' , 'color']
    ordering_fields = [ 'price', 'created_at']
    

       
         
  
        
        
        
    
    
