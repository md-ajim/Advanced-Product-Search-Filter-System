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

# NEW Test data for Products with real image URLs (30 products)
products_data = [
    # Clothes - 6 products
    {
        "name": "Casual Blazer",
        "title": "Men's Slim Blazer",
        "category_name": "CLOTHES",
        "description": "Elegant slim-fit blazer perfect for business casual occasions",
        "price": Decimal("89.99"),
        "size": "L",
        "color": "Navy",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&q=80"
    },
    {
        "name": "Knit Sweater",
        "title": "Cozy Pullover",
        "category_name": "CLOTHES",
        "description": "Warm cable-knit sweater for cold weather comfort",
        "price": Decimal("42.99"),
        "size": "M",
        "color": "Burgundy",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=800&q=80"
    },
    {
        "name": "Cargo Shorts",
        "title": "Summer Shorts",
        "category_name": "CLOTHES",
        "description": "Comfortable cargo shorts with multiple pockets",
        "price": Decimal("34.99"),
        "size": "32",
        "color": "Olive",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=800&q=80"
    },
    {
        "name": "Athletic Leggings",
        "title": "Workout Tights",
        "category_name": "CLOTHES",
        "description": "High-waist athletic leggings with moisture-wicking fabric",
        "price": Decimal("38.99"),
        "size": "S",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=800&q=80"
    },
    {
        "name": "Denim Jacket",
        "title": "Classic Jean Jacket",
        "category_name": "CLOTHES",
        "description": "Timeless denim jacket with button closure",
        "price": Decimal("59.99"),
        "size": "M",
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=800&q=80"
    },
    {
        "name": "Ankle Boots",
        "title": "Leather Boots",
        "category_name": "CLOTHES",
        "description": "Genuine leather ankle boots with side zipper",
        "price": Decimal("94.99"),
        "size": "9",
        "color": "Brown",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=800&q=80"
    },
    
    # Home Interiors - 6 products
    {
        "name": "Pendant Light",
        "title": "Modern Chandelier",
        "category_name": "HOME",
        "description": "Elegant crystal pendant light for dining room",
        "price": Decimal("129.99"),
        "size": "24 inch",
        "color": "Chrome",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1567225477277-c1c5b3e0d9d1?w=800&q=80"
    },
    {
        "name": "Accent Chair",
        "title": "Mid-Century Chair",
        "category_name": "HOME",
        "description": "Stylish mid-century modern accent chair with wooden legs",
        "price": Decimal("189.99"),
        "size": None,
        "color": "Mustard",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=800&q=80"
    },
    {
        "name": "Side Table",
        "title": "Nightstand",
        "category_name": "HOME",
        "description": "Compact side table with drawer storage",
        "price": Decimal("79.99"),
        "size": "18x18",
        "color": "White",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800&q=80"
    },
    {
        "name": "Wall Clock",
        "title": "Vintage Clock",
        "category_name": "HOME",
        "description": "Large vintage-style wall clock with Roman numerals",
        "price": Decimal("44.99"),
        "size": "20 inch",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=800&q=80"
    },
    {
        "name": "Throw Blanket",
        "title": "Soft Blanket",
        "category_name": "HOME",
        "description": "Ultra-soft fleece throw blanket for couch",
        "price": Decimal("29.99"),
        "size": "50x60",
        "color": "Gray",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=800&q=80"
    },
    {
        "name": "Picture Frame Set",
        "title": "Gallery Frames",
        "category_name": "HOME",
        "description": "Set of 5 black picture frames in various sizes",
        "price": Decimal("39.99"),
        "size": "Multi",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1582053433976-25c00369fc93?w=800&q=80"
    },
    
    # Electronics - 6 products
    {
        "name": "Wireless Charger",
        "title": "Fast Charging Pad",
        "category_name": "ELECTRONICS",
        "description": "Qi wireless charging pad with LED indicator",
        "price": Decimal("24.99"),
        "size": None,
        "color": "White",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1591290619762-71d1e58e7a1b?w=800&q=80"
    },
    {
        "name": "Gaming Headset",
        "title": "RGB Headphones",
        "category_name": "ELECTRONICS",
        "description": "7.1 surround sound gaming headset with microphone",
        "price": Decimal("79.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1599669454699-248893623440?w=800&q=80"
    },
    {
        "name": "Phone Case",
        "title": "Protective Case",
        "category_name": "ELECTRONICS",
        "description": "Shockproof phone case with raised edges",
        "price": Decimal("14.99"),
        "size": "iPhone",
        "color": "Clear",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=800&q=80"
    },
    {
        "name": "Smart LED Bulb",
        "title": "WiFi Light Bulb",
        "category_name": "ELECTRONICS",
        "description": "Color-changing smart bulb compatible with Alexa",
        "price": Decimal("19.99"),
        "size": "E26",
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1550985616-10810253b84d?w=800&q=80"
    },
    {
        "name": "Desk Monitor",
        "title": "24-inch Display",
        "category_name": "ELECTRONICS",
        "description": "Full HD IPS monitor with ultra-thin bezels",
        "price": Decimal("159.99"),
        "size": "24 inch",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&q=80"
    },
    {
        "name": "External SSD",
        "title": "Portable Drive",
        "category_name": "ELECTRONICS",
        "description": "1TB portable SSD with USB-C connection",
        "price": Decimal("99.99"),
        "size": "1TB",
        "color": "Gray",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=800&q=80"
    },
    
    # Beauty & Health - 6 products
    {
        "name": "Lip Gloss Set",
        "title": "Shine Collection",
        "category_name": "BEAUTY",
        "description": "Set of 6 moisturizing lip glosses in trendy shades",
        "price": Decimal("26.99"),
        "size": "6x8ml",
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&q=80"
    },
    {
        "name": "Eyeshadow Palette",
        "title": "Nude Palette",
        "category_name": "BEAUTY",
        "description": "18-color eyeshadow palette with mirror",
        "price": Decimal("32.99"),
        "size": "18 colors",
        "color": "Neutral",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=800&q=80"
    },
    {
        "name": "Micellar Water",
        "title": "Makeup Remover",
        "category_name": "BEAUTY",
        "description": "Gentle micellar water for all skin types",
        "price": Decimal("16.99"),
        "size": "400ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=800&q=80"
    },
    {
        "name": "Hair Straightener",
        "title": "Ceramic Iron",
        "category_name": "BEAUTY",
        "description": "Professional ceramic hair straightener with adjustable temperature",
        "price": Decimal("49.99"),
        "size": None,
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1526045478516-99145907023c?w=800&q=80"
    },
    {
        "name": "Face Cream",
        "title": "Anti-Aging Cream",
        "category_name": "BEAUTY",
        "description": "Retinol night cream for fine lines and wrinkles",
        "price": Decimal("39.99"),
        "size": "50ml",
        "color": None,
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1556228852-80f5ac04fa36?w=800&q=80"
    },
    {
        "name": "Bath Bombs",
        "title": "Spa Set",
        "category_name": "BEAUTY",
        "description": "Luxury bath bomb set with essential oils",
        "price": Decimal("21.99"),
        "size": "6 pack",
        "color": "Multi",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=800&q=80"
    },
    
    # Sports & Outdoors - 6 products
    {
        "name": "Bike Helmet",
        "title": "Safety Helmet",
        "category_name": "SPORTS",
        "description": "Adjustable cycling helmet with ventilation",
        "price": Decimal("39.99"),
        "size": "Adult",
        "color": "Red",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1565641379548-67006a29f9f3?w=800&q=80"
    },
    {
        "name": "Camping Tent",
        "title": "4-Person Tent",
        "category_name": "SPORTS",
        "description": "Waterproof camping tent with easy setup",
        "price": Decimal("129.99"),
        "size": "4 person",
        "color": "Green",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?w=800&q=80"
    },
    {
        "name": "Soccer Ball",
        "title": "Match Ball",
        "category_name": "SPORTS",
        "description": "Official size 5 soccer ball for training and matches",
        "price": Decimal("24.99"),
        "size": "Size 5",
        "color": "White",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1614632537197-38a17061c2bd?w=800&q=80"
    },
    {
        "name": "Yoga Block",
        "title": "Foam Block",
        "category_name": "SPORTS",
        "description": "High-density EVA foam yoga block for support",
        "price": Decimal("12.99"),
        "size": "9x6x4",
        "color": "Purple",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1588286840104-8957b019727f?w=800&q=80"
    },
    {
        "name": "Protein Shaker",
        "title": "Blender Bottle",
        "category_name": "SPORTS",
        "description": "Leak-proof protein shaker with mixing ball",
        "price": Decimal("9.99"),
        "size": "28oz",
        "color": "Black",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1594737626072-90dc274bc2bd?w=800&q=80"
    },
    {
        "name": "Swimming Goggles",
        "title": "Anti-Fog Goggles",
        "category_name": "SPORTS",
        "description": "UV protection swimming goggles with adjustable strap",
        "price": Decimal("19.99"),
        "size": "Adult",
        "color": "Blue",
        "is_active": True,
        "image_url": "https://images.unsplash.com/photo-1519315901367-f34ff9154487?w=800&q=80"
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
    Add NEW test data without removing existing data.
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
    print("ADDING NEW TEST DATA (KEEPING EXISTING DATA)")
    print("="*70)
    print(f"Max dimensions: {max_width}x{max_height}")
    print("Images smaller than max will keep original size")
    print("Images larger than max will be resized proportionally")
    print("="*70)
    
    # Get or create categories (don't delete existing ones)
    category_objects = {}
    print("\nChecking categories...")
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={"title": cat_data["title"]}
        )
        category_objects[cat_data["name"]] = category
        if created:
            print(f"  ✓ Created: {category.name}")
        else:
            print(f"  ✓ Exists: {category.name}")
    
    print(f"\n{'='*70}")
    print("DOWNLOADING AND PROCESSING NEW PRODUCTS")
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
            filename = f"{prod_data['name'].lower().replace(' ', '_')}_{timezone.now().timestamp()}.jpg"
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
    print(f"✓ Total Categories: {Category.objects.count()}")
    print(f"✓ Total Products in Database: {Product.objects.count()}")
    print(f"✓ NEW Products Added: {success_count}")
    print(f"  • Images resized: {resized_count}")
    print(f"  • Original size kept: {kept_original_count}")
    if fail_count > 0:
        print(f"✗ Failed downloads: {fail_count}")
    
    if success_count > 0:
        print(f"\n📊 STORAGE OPTIMIZATION (NEW PRODUCTS):")
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
# Save as: your_app/management/commands/add_test_data.py

from django.core.management.base import BaseCommand
from your_app.test_data import create_test_data

class Command(BaseCommand):
    help = 'Add NEW test data without removing existing products'

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
        
        self.stdout.write(self.style.WARNING(f'Adding new test data (max: {max_width}x{max_height})...'))
        create_test_data(max_width=max_width, max_height=max_height)
        self.stdout.write(self.style.SUCCESS('✓ Complete!'))

# Usage:
# python manage.py add_test_data
# python manage.py add_test_data --max-width 1200 --max-height 900
"""