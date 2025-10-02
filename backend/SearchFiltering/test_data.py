from django.core.files.base import ContentFile
from decimal import Decimal
from django.utils import timezone
import requests
from io import BytesIO

# Test data for Categories
categories_data = [
    {
        "name": "ALL",
        "title": "Browse All Products"
    },
    {
        "name": "CLOTHES",
        "title": "Fashion & Apparel"
    },
    {
        "name": "HOME",
        "title": "Home Decor & Furniture"
    },
    {
        "name": "ELECTRONICS",
        "title": "Tech & Gadgets"
    },
    {
        "name": "BEAUTY",
        "title": "Beauty & Wellness"
    },
    {
        "name": "SPORTS",
        "title": "Fitness & Adventure"
    }
]

# Test data for Products with real image URLs
products_data = [
    # Clothes
    {
        "name": "Cotton T-Shirt",
        "title": "Classic Cotton Tee",
        "category_name": "CLOTHES",
        "description": "Comfortable 100% cotton t-shirt perfect for everyday wear",
        "price": Decimal("19.99"),
        "size": "M",
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&q=80"
    },
    {
        "name": "Denim Jeans",
        "title": "Slim Fit Jeans",
        "category_name": "CLOTHES",
        "description": "Modern slim fit denim jeans with stretch fabric",
        "price": Decimal("49.99"),
        "size": "32",
        "color": "Dark Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=800&q=80"
    },
    {
        "name": "Summer Dress",
        "title": "Floral Maxi Dress",
        "category_name": "CLOTHES",
        "description": "Lightweight floral print maxi dress for summer",
        "price": Decimal("39.99"),
        "size": "L",
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=800&q=80"
    },
    {
        "name": "Leather Jacket",
        "title": "Biker Jacket",
        "category_name": "CLOTHES",
        "description": "Genuine leather jacket with zipper details",
        "price": Decimal("129.99"),
        "size": "L",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800&q=80"
    },
    {
        "name": "Sneakers",
        "title": "White Sneakers",
        "category_name": "CLOTHES",
        "description": "Classic white sneakers for casual wear",
        "price": Decimal("59.99"),
        "size": "9",
        "color": "White",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=800&q=80"
    },
    
    # Home Interiors
    {
        "name": "Table Lamp",
        "title": "Modern LED Lamp",
        "category_name": "HOME",
        "description": "Energy-efficient LED table lamp with adjustable brightness",
        "price": Decimal("29.99"),
        "size": None,
        "color": "White",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800&q=80"
    },
    {
        "name": "Throw Pillow",
        "title": "Velvet Cushion",
        "category_name": "HOME",
        "description": "Soft velvet throw pillow with removable cover",
        "price": Decimal("15.99"),
        "size": "18x18",
        "color": "Gray",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=800&q=80"
    },
    {
        "name": "Wall Art",
        "title": "Abstract Canvas",
        "category_name": "HOME",
        "description": "Contemporary abstract art canvas print",
        "price": Decimal("79.99"),
        "size": "24x36",
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1547826039-bfc35e0f1ea8?w=800&q=80"
    },
    {
        "name": "Coffee Table",
        "title": "Modern Oak Table",
        "category_name": "HOME",
        "description": "Solid oak coffee table with minimalist design",
        "price": Decimal("149.99"),
        "size": "48x24",
        "color": "Natural",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1532372320572-cda25653a26d?w=800&q=80"
    },
    {
        "name": "Plant Pot",
        "title": "Ceramic Planter",
        "category_name": "HOME",
        "description": "Handmade ceramic plant pot with drainage hole",
        "price": Decimal("24.99"),
        "size": "8 inch",
        "color": "Terracotta",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800&q=80"
    },
    
    # Electronics
    {
        "name": "Wireless Earbuds",
        "title": "Pro Earbuds",
        "category_name": "ELECTRONICS",
        "description": "Bluetooth 5.0 wireless earbuds with noise cancellation",
        "price": Decimal("89.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800&q=80"
    },
    {
        "name": "Smart Watch",
        "title": "Fitness Tracker",
        "category_name": "ELECTRONICS",
        "description": "Waterproof smartwatch with heart rate monitor",
        "price": Decimal("149.99"),
        "size": "42mm",
        "color": "Silver",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&q=80"
    },
    {
        "name": "Laptop Stand",
        "title": "Aluminum Stand",
        "category_name": "ELECTRONICS",
        "description": "Ergonomic aluminum laptop stand with adjustable height",
        "price": Decimal("34.99"),
        "size": None,
        "color": "Silver",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800&q=80"
    },
    {
        "name": "Bluetooth Speaker",
        "title": "Portable Speaker",
        "category_name": "ELECTRONICS",
        "description": "Waterproof portable speaker with 360-degree sound",
        "price": Decimal("69.99"),
        "size": None,
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800&q=80"
    },
    {
        "name": "Wireless Mouse",
        "title": "Ergonomic Mouse",
        "category_name": "ELECTRONICS",
        "description": "Wireless ergonomic mouse with adjustable DPI",
        "price": Decimal("29.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=800&q=80"
    },
    
    # Beauty & Health
    {
        "name": "Face Serum",
        "title": "Vitamin C Serum",
        "category_name": "BEAUTY",
        "description": "Anti-aging vitamin C face serum for bright skin",
        "price": Decimal("34.99"),
        "size": "30ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=800&q=80"
    },
    {
        "name": "Hair Dryer",
        "title": "Ionic Hair Dryer",
        "category_name": "BEAUTY",
        "description": "Professional ionic hair dryer with multiple heat settings",
        "price": Decimal("59.99"),
        "size": None,
        "color": "Rose Gold",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=800&q=80"
    },
    {
        "name": "Moisturizer",
        "title": "Daily Hydrator",
        "category_name": "BEAUTY",
        "description": "Lightweight daily moisturizer for all skin types",
        "price": Decimal("22.99"),
        "size": "50ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=800&q=80"
    },
    {
        "name": "Makeup Brush Set",
        "title": "Pro Brush Kit",
        "category_name": "BEAUTY",
        "description": "12-piece professional makeup brush set with case",
        "price": Decimal("44.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=800&q=80"
    },
    {
        "name": "Essential Oils",
        "title": "Aromatherapy Set",
        "category_name": "BEAUTY",
        "description": "Set of 6 pure essential oils for relaxation",
        "price": Decimal("39.99"),
        "size": "10ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=800&q=80"
    },
    
    # Sports & Outdoors
    {
        "name": "Yoga Mat",
        "title": "Premium Mat",
        "category_name": "SPORTS",
        "description": "Non-slip yoga mat with carrying strap",
        "price": Decimal("29.99"),
        "size": "6ft",
        "color": "Purple",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=800&q=80"
    },
    {
        "name": "Water Bottle",
        "title": "Insulated Bottle",
        "category_name": "SPORTS",
        "description": "Stainless steel insulated water bottle keeps drinks cold for 24h",
        "price": Decimal("19.99"),
        "size": "32oz",
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800&q=80"
    },
    {
        "name": "Running Shoes",
        "title": "Trail Runners",
        "category_name": "SPORTS",
        "description": "Lightweight trail running shoes with excellent grip",
        "price": Decimal("79.99"),
        "size": "10",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&q=80"
    },
    {
        "name": "Dumbbells Set",
        "title": "Adjustable Weights",
        "category_name": "SPORTS",
        "description": "Adjustable dumbbell set 5-25 lbs with storage rack",
        "price": Decimal("99.99"),
        "size": None,
        "color": "Gray",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=800&q=80"
    },
    {
        "name": "Resistance Bands",
        "title": "Exercise Bands",
        "category_name": "SPORTS",
        "description": "Set of 5 resistance bands for strength training",
        "price": Decimal("24.99"),
        "size": None,
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1598632640487-6ea4a4e8b963?w=800&q=80"
    }
]


def download_image(url, timeout=10):
    """
    Download image from URL and return as ContentFile
    """
    try:
        response = requests.get(url, timeout=timeout, stream=True)
        response.raise_for_status()
        
        # Read image content
        image_content = BytesIO(response.content)
        return image_content.read()
    except Exception as e:
        print(f"Error downloading image from {url}: {str(e)}")
        return None


def create_test_data():
    """
    Run this function in Django shell or management command to populate database
    Usage: python manage.py shell
    >>> from your_app.test_data import create_test_data
    >>> create_test_data()
    
    Note: Make sure 'requests' library is installed: pip install requests
    """
    from SearchFiltering.models import Category, Product
    
    print("Starting test data creation...")
    print("="*60)
    
    # Clear existing data (optional)
    Product.objects.all().delete()
    Category.objects.all().delete()
    print("Cleared existing data\n")
    
    # Create categories
    category_objects = {}
    print("Creating categories...")
    for cat_data in categories_data:
        category = Category.objects.create(**cat_data)
        category_objects[cat_data["name"]] = category
        print(f"  ✓ Created category: {category.name}")
    
    print(f"\n{'='*60}")
    print("Downloading images and creating products...")
    print(f"{'='*60}\n")
    
    # Create products with real images
    success_count = 0
    fail_count = 0
    
    for i, prod_data in enumerate(products_data, 1):
        category_name = prod_data.pop("category_name")
        image_url = prod_data.pop("image_url")
        
        print(f"[{i}/{len(products_data)}] Processing: {prod_data['title']}")
        
        # Download image
        image_data = download_image(image_url)
        
        if image_data:
            # Create product with image
            filename = f"{prod_data['name'].lower().replace(' ', '_')}.jpg"
            
            product = Product.objects.create(
                category=category_objects[category_name],
                created_at=timezone.now(),
                **prod_data
            )
            
            # Save image to product
            product.image.save(filename, ContentFile(image_data), save=True)
            
            print(f"  ✓ Created with image ({len(image_data)} bytes)")
            success_count += 1
        else:
            # Create product without image
            product = Product.objects.create(
                category=category_objects[category_name],
                created_at=timezone.now(),
                **prod_data
            )
            print(f"  ⚠ Created without image (download failed)")
            fail_count += 1
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"✓ Total Categories: {Category.objects.count()}")
    print(f"✓ Total Products: {Product.objects.count()}")
    print(f"✓ Products with images: {success_count}")
    if fail_count > 0:
        print(f"⚠ Products without images: {fail_count}")
    print(f"{'='*60}")


# Management Command Template
MANAGEMENT_COMMAND = """
# Save this as: your_app/management/commands/load_test_data.py

from django.core.management.base import BaseCommand
from SearchFiltering.test_data import create_test_data

class Command(BaseCommand):
    help = 'Load test data for products and categories with real images'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Loading test data...'))
        create_test_data()
        self.stdout.write(self.style.SUCCESS('\\n✓ Test data loaded successfully!'))

# Usage: python manage.py load_test_data
"""