
from rest_framework import serializers
from .models import Product , Category , Review





class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = '__all__'
       
       
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'        
               
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True)
 
    
    
    class Meta:
        model = Product
        fields = '__all__'
        
        

