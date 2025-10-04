import django_filters 
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', label='Category')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    rating = django_filters.NumberFilter(field_name='reviews__rating', label='Rating')


    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'rating']
