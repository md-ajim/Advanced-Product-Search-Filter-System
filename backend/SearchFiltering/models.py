from django.db import models



class Category(models.Model):
      CATEGORY_CHOICES = [
        ("ALL", "All Categories"),
        ("CLOTHES", "Clothes and Wear"),
        ("HOME", "Home Interiors"),
        ("ELECTRONICS", "Electronics"),
        ("BEAUTY", "Beauty & Health"),
        ("SPORTS", "Sports & Outdoors"),
    ]
      name = models.CharField(max_length=100, choices=CATEGORY_CHOICES , default='ALL' )
      title = models.CharField( max_length=200 , null=True, blank=True)
      
      def __str__(self) -> str:
        return self.name if self.name else "Unnamed Category"

    

class Product(models.Model):
    
    name = models.CharField( max_length=255)
    title = models.CharField( max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    size = models.CharField(max_length=10 , null=True , blank=True)
    color = models.CharField(max_length=10, null=True , blank=True)
    image = models.ImageField(upload_to='images', blank=True , null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title







class Review(models.Model):
    SORTING_CHOICES = [
        ('newest', 'Newest'),
        ('oldest', 'Oldest'),
        ('highest-rating', 'Highest Rating'),
        ('lowest-rating', 'Lowest Rating'),
        ('most-helpful', 'Most Helpful'),
    ]

    sort_by = models.CharField(max_length=50, choices=SORTING_CHOICES, default='newest')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # Scale 1-5
    comment = models.TextField()
    helpful_votes = models.PositiveIntegerField(default=0)
    reported = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.comment
    