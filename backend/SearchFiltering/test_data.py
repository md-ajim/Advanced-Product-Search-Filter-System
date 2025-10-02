from django.core.files.base import ContentFile
from decimal import Decimal
from django.utils import timezone
import requests
from io import BytesIO
from PIL import Image

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

# NEW Test data for Products with real image URLs
products_data = [
    # Clothes - NEW PRODUCTS
    {
        "name": "Hooded Sweatshirt",
        "title": "Urban Hoodie",
        "category_name": "CLOTHES",
        "description": "Premium cotton blend hoodie with front pocket and adjustable drawstring",
        "price": Decimal("45.99"),
        "size": "L",
        "color": "Gray",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800&q=80"
    },
    {
        "name": "Chino Pants",
        "title": "Slim Chinos",
        "category_name": "CLOTHES",
        "description": "Versatile slim-fit chino pants perfect for casual or semi-formal wear",
        "price": Decimal("54.99"),
        "size": "32",
        "color": "Khaki",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=800&q=80"
    },
    {
        "name": "Winter Coat",
        "title": "Wool Overcoat",
        "category_name": "CLOTHES",
        "description": "Classic wool blend overcoat with button closure and side pockets",
        "price": Decimal("159.99"),
        "size": "M",
        "color": "Navy",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1539533113208-f6df8cc8b543?w=800&q=80"
    },
    {
        "name": "Polo Shirt",
        "title": "Classic Polo",
        "category_name": "CLOTHES",
        "description": "Cotton pique polo shirt with three-button placket",
        "price": Decimal("29.99"),
        "size": "M",
        "color": "White",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1586363104862-3a5e2ab60d99?w=800&q=80"
    },
    {
        "name": "Canvas Backpack",
        "title": "Travel Backpack",
        "category_name": "CLOTHES",
        "description": "Durable canvas backpack with laptop compartment and multiple pockets",
        "price": Decimal("69.99"),
        "size": "15L",
        "color": "Olive",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&q=80"
    },
    
    # Home Interiors - NEW PRODUCTS
    {
        "name": "Floor Lamp",
        "title": "Arc Floor Lamp",
        "category_name": "HOME",
        "description": "Modern arc floor lamp with marble base and adjustable height",
        "price": Decimal("89.99"),
        "size": "72 inch",
        "color": "Gold",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=800&q=80"
    },
    {
        "name": "Wall Mirror",
        "title": "Round Mirror",
        "category_name": "HOME",
        "description": "Large round wall mirror with gold metal frame",
        "price": Decimal("79.99"),
        "size": "32 inch",
        "color": "Gold",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1618220179428-22790b461013?w=800&q=80"
    },
    {
        "name": "Bookshelf",
        "title": "Modern Shelf",
        "category_name": "HOME",
        "description": "5-tier wooden bookshelf with industrial metal frame",
        "price": Decimal("129.99"),
        "size": "72x36",
        "color": "Walnut",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1594620302200-9a762244a156?w=800&q=80"
    },
    {
        "name": "Dining Chair",
        "title": "Velvet Chair",
        "category_name": "HOME",
        "description": "Upholstered velvet dining chair with wooden legs",
        "price": Decimal("119.99"),
        "size": None,
        "color": "Emerald",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800&q=80"
    },
    {
        "name": "Area Rug",
        "title": "Geometric Rug",
        "category_name": "HOME",
        "description": "Contemporary geometric pattern area rug in neutral tones",
        "price": Decimal("189.99"),
        "size": "8x10",
        "color": "Beige",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1600166898405-da9535204843?w=800&q=80"
    },
    
    # Electronics - NEW PRODUCTS
    {
        "name": "Mechanical Keyboard",
        "title": "RGB Keyboard",
        "category_name": "ELECTRONICS",
        "description": "Gaming mechanical keyboard with RGB backlight and brown switches",
        "price": Decimal("119.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&q=80"
    },
    {
        "name": "Webcam",
        "title": "HD Webcam",
        "category_name": "ELECTRONICS",
        "description": "1080p HD webcam with autofocus and built-in microphone",
        "price": Decimal("79.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1625948515291-69613efd103f?w=800&q=80"
    },
    {
        "name": "Tablet Stand",
        "title": "Adjustable Stand",
        "category_name": "ELECTRONICS",
        "description": "Universal tablet stand with 360-degree rotation",
        "price": Decimal("24.99"),
        "size": None,
        "color": "Silver",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&q=80"
    },
    {
        "name": "Power Bank",
        "title": "20000mAh Charger",
        "category_name": "ELECTRONICS",
        "description": "High-capacity power bank with fast charging and dual USB ports",
        "price": Decimal("39.99"),
        "size": "20000mAh",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=800&q=80"
    },
    {
        "name": "USB Hub",
        "title": "7-Port Hub",
        "category_name": "ELECTRONICS",
        "description": "USB 3.0 hub with 7 ports and individual power switches",
        "price": Decimal("29.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1625948515291-69613efd103f?w=800&q=80"
    },
    
    # Beauty & Health - NEW PRODUCTS
    {
        "name": "Face Mask Set",
        "title": "Hydrating Masks",
        "category_name": "BEAUTY",
        "description": "Pack of 10 hydrating sheet masks with hyaluronic acid",
        "price": Decimal("24.99"),
        "size": "10 pack",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=800&q=80"
    },
    {
        "name": "Nail Polish Set",
        "title": "Classic Colors",
        "category_name": "BEAUTY",
        "description": "Set of 5 long-lasting nail polish in classic shades",
        "price": Decimal("29.99"),
        "size": "5x15ml",
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1610992015732-2449b76344bc?w=800&q=80"
    },
    {
        "name": "Facial Roller",
        "title": "Jade Roller",
        "category_name": "BEAUTY",
        "description": "Natural jade facial roller for massage and lymphatic drainage",
        "price": Decimal("19.99"),
        "size": None,
        "color": "Green",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=800&q=80"
    },
    {
        "name": "Perfume",
        "title": "Floral Essence",
        "category_name": "BEAUTY",
        "description": "Elegant floral fragrance with notes of jasmine and rose",
        "price": Decimal("64.99"),
        "size": "50ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=800&q=80"
    },
    {
        "name": "Body Lotion",
        "title": "Shea Butter Cream",
        "category_name": "BEAUTY",
        "description": "Rich moisturizing body lotion with shea butter and vitamin E",
        "price": Decimal("18.99"),
        "size": "200ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=800&q=80"
    },
    
    # Sports & Outdoors - NEW PRODUCTS
    {
        "name": "Jump Rope",
        "title": "Speed Rope",
        "category_name": "SPORTS",
        "description": "Adjustable speed jump rope with ball bearings for smooth rotation",
        "price": Decimal("14.99"),
        "size": "9ft",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1517836477839-7072aaa8b121?w=800&q=80"
    },
    {
        "name": "Foam Roller",
        "title": "Muscle Roller",
        "category_name": "SPORTS",
        "description": "High-density foam roller for muscle recovery and massage",
        "price": Decimal("24.99"),
        "size": "18 inch",
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1599058917212-d750089bc07e?w=800&q=80"
    },
    {
        "name": "Gym Bag",
        "title": "Duffel Bag",
        "category_name": "SPORTS",
        "description": "Large duffel bag with shoe compartment and water-resistant material",
        "price": Decimal("49.99"),
        "size": "50L",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&q=80"
    },
    {
        "name": "Boxing Gloves",
        "title": "Training Gloves",
        "category_name": "SPORTS",
        "description": "Professional boxing gloves with wrist support and padding",
        "price": Decimal("59.99"),
        "size": "14oz",
        "color": "Red",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1517438476312-10d79c077509?w=800&q=80"
    },
    {
        "name": "Tennis Racket",
        "title": "Pro Racket",
        "category_name": "SPORTS",
        "description": "Lightweight carbon fiber tennis racket with overgrip",
        "price": Decimal("89.99"),
        "size": "27 inch",
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1622163642998-1ea32b0bbc67?w=800&q=80"
    }
]


def download_image(url, timeout=10):
    """
    Download image from URL and return as bytes
    """
    try:
        response = requests.get(url, timeout=timeout, stream=True)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"  ⚠ Error downloading image: {str(e)}")
        return None


def smart_resize_image(image_data, max_width=800, max_height=600):
    """
    Intelligently resize image ONLY if it exceeds max dimensions.
    If image is smaller than max dimensions, keep original size.
    
    Args:
        image_data: Image bytes
        max_width: Maximum allowed width (default 800)
        max_height: Maximum allowed height (default 600)
    
    Returns:
        Resized image bytes (or original if smaller)
    """
    try:
        # Open image from bytes
        img = Image.open(BytesIO(image_data))
        original_width, original_height = img.size
        
        # Convert RGBA to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Check if image exceeds max dimensions
        if original_width > max_width or original_height > max_height:
            # Calculate resize ratio to maintain aspect ratio
            width_ratio = max_width / original_width
            height_ratio = max_height / original_height
            resize_ratio = min(width_ratio, height_ratio)
            
            new_width = int(original_width * resize_ratio)
            new_height = int(original_height * resize_ratio)
            
            # Resize image
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save to bytes
            output = BytesIO()
            img.save(output, format='JPEG', quality=85, optimize=True)
            output.seek(0)
            
            return output.read(), True, (original_width, original_height), (new_width, new_height)
        else:
            # Image is smaller than max dimensions, keep original
            output = BytesIO()
            img.save(output, format='JPEG', quality=85, optimize=True)
            output.seek(0)
            
            return output.read(), False, (original_width, original_height), (original_width, original_height)
            
    except Exception as e:
        print(f"  ⚠ Error processing image: {str(e)}")
        return image_data, False, (0, 0), (0, 0)


def create_test_data(max_width=800, max_height=600):
    """
    Run this function in Django shell or management command to populate database
    Images will keep their original size if smaller than max dimensions.
    Images will be resized ONLY if they exceed max dimensions.
    
    Args:
        max_width: Maximum allowed width (default 800)
        max_height: Maximum allowed height (default 600)
    
    Usage: 
        python manage.py shell
        >>> from your_app.test_data import create_test_data
        >>> create_test_data()  # Default: max 800x600
        >>> create_test_data(max_width=1200, max_height=900)  # Custom max size
    
    Note: Make sure libraries are installed: pip install requests Pillow
    """
    from SearchFiltering.models import Category, Product
    
    print("="*70)
    print("STARTING TEST DATA CREATION WITH NEW PRODUCTS")
    print("="*70)
    print(f"Max dimensions: {max_width}x{max_height}")
    print("Images smaller than max will keep original size")
    print("Images larger than max will be resized proportionally")
    print("="*70)
    
    # Clear existing data
    Product.objects.all().delete()
    Category.objects.all().delete()
    print("\n✓ Cleared existing data\n")
    
    # Create categories
    category_objects = {}
    print("Creating categories...")
    for cat_data in categories_data:
        category = Category.objects.create(**cat_data)
        category_objects[cat_data["name"]] = category
        print(f"  ✓ {category.name}")
    
    print(f"\n{'='*70}")
    print("DOWNLOADING AND PROCESSING IMAGES")
    print(f"{'='*70}\n")
    
    # Statistics
    success_count = 0
    fail_count = 0
    resized_count = 0
    kept_original_count = 0
    total_size_before = 0
    total_size_after = 0
    
    for i, prod_data in enumerate(products_data, 1):
        category_name = prod_data.pop("category_name")
        image_url = prod_data.pop("image_url")
        
        print(f"[{i}/{len(products_data)}] {prod_data['title']}")
        
        # Download image
        image_data = download_image(image_url)
        
        if image_data:
            original_size = len(image_data)
            total_size_before += original_size
            
            # Smart resize (only if needed)
            processed_data, was_resized, orig_dims, new_dims = smart_resize_image(
                image_data, max_width, max_height
            )
            
            final_size = len(processed_data)
            total_size_after += final_size
            
            # Create product
            filename = f"{prod_data['name'].lower().replace(' ', '_')}.jpg"
            product = Product.objects.create(
                category=category_objects[category_name],
                created_at=timezone.now(),
                **prod_data
            )
            product.image.save(filename, ContentFile(processed_data), save=True)
            
            # Display info
            if was_resized:
                print(f"  ✓ Resized: {orig_dims[0]}x{orig_dims[1]} → {new_dims[0]}x{new_dims[1]} ({original_size//1024}KB → {final_size//1024}KB)")
                resized_count += 1
            else:
                print(f"  ✓ Original kept: {orig_dims[0]}x{orig_dims[1]} ({final_size//1024}KB)")
                kept_original_count += 1
            
            success_count += 1
        else:
            # Create product without image
            product = Product.objects.create(
                category=category_objects[category_name],
                created_at=timezone.now(),
                **prod_data
            )
            print(f"  ✗ Failed to download")
            fail_count += 1
    
    # Final Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"✓ Categories created: {Category.objects.count()}")
    print(f"✓ Products created: {Product.objects.count()}")
    print(f"✓ Products with images: {success_count}")
    print(f"  • Images resized: {resized_count}")
    print(f"  • Original size kept: {kept_original_count}")
    if fail_count > 0:
        print(f"✗ Failed downloads: {fail_count}")
    
    if success_count > 0:
        print(f"\n📊 STORAGE OPTIMIZATION:")
        print(f"   Total before: {total_size_before//1024}KB")
        print(f"   Total after: {total_size_after//1024}KB")
        if total_size_before > total_size_after:
            savings = ((total_size_before - total_size_after) / total_size_before * 100)
            print(f"   Saved: {savings:.1f}%")
        else:
            print(f"   No compression needed")
    print(f"{'='*70}\n")


# Management Command
MANAGEMENT_COMMAND = """
# Save as: your_app/management/commands/load_test_data.py

from django.core.management.base import BaseCommand
from your_app.test_data import create_test_data

class Command(BaseCommand):
    help = 'Load NEW test data with smart image resizing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-width',
            type=int,
            default=800,
            help='Maximum image width (default: 800)'
        )
        parser.add_argument(
            '--max-height',
            type=int,
            default=600,
            help='Maximum image height (default: 600)'
        )

    def handle(self, *args, **options):
        max_width = options['max_width']
        max_height = options['max_height']
        
        self.stdout.write(self.style.WARNING(f'Loading test data (max: {max_width}x{max_height})...'))
        create_test_data(max_width=max_width, max_height=max_height)
        self.stdout.write(self.style.SUCCESS('✓ Complete!'))

# Usage:
# python manage.py load_test_data
# python manage.py load_test_data --max-width 1200 --max-height 900
"""