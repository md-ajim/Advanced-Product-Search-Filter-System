# 🔍 Advanced Product Search & Filter System – Full-Stack Portfolio Project

This is a full-stack portfolio project built with **Django REST Framework**, **MySQL**, **Django Unfold**, **Next.js App Router**, **Tailwind CSS**, and **Shadcn UI**. It showcases a robust and scalable **search and filtering system** for products using **django-filter**, dynamic query handling, and a modern, animated frontend.

> ⚡ This project demonstrates my skills as a **Full-Stack Developer**, capable of building optimized APIs, integrating advanced search filters, and designing interactive user interfaces with professional UI libraries.

---

## ✨ Key Features

### 🔧 Backend (Django + DRF + MySQL)
- **Product Filtering** using `django-filter` with custom filters:
  - Category filter
  - Price range (min, max)
  - Product rating
- **Advanced Search** with `SearchFilter` and `OrderingFilter`
- **Clean API design** with `ListAPIView`
- **Admin UI customization** using [Django Unfold](https://github.com/unfoldadmin/unfold)
- **MySQL** database for relational data and performance

### 💻 Frontend (Next.js App Router + Tailwind CSS + Shadcn UI)
- Fully dynamic frontend using **Next.js App Router**
- **Interactive UI** with **Shadcn UI** components
- Responsive filtering UI for category, price range, and rating
- Live search functionality with debounce
- Mobile-first design with **Tailwind CSS**
- API consumption from DRF with real-time filter response

---

## 📂 Code Highlights

### filters.py

```python
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
views.py
class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().distinct()
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'price', 'color']
    ordering_fields = ['price', 'created_at']

🚀 How to Run
🛠 Backend Setup

git clone https://github.com/your-username/your-repo-name.git
cd your-backend-directory
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


🌐 Frontend Setup

cd frontend
npm install
npm run dev


🧠 Why This Project Matters
This project reflects:

📊 Real-world eCommerce use case

🎯 Precision filtering logic handled at backend level

🧩 Decoupled architecture with DRF + Next.js

🎨 Modern UI design using industry-standard Shadcn UI and Tailwind CSS

🔄 Live search, filtering, and sorting powered by clean REST API

👨‍💻 About Me
I’m a results-driven Full-Stack Developer passionate about building high-performance, scalable, and user-centric web applications. I specialize in:

🔗 Next.js, Tailwind, Shadcn UI

🛠 Django REST Framework, MySQL, JWT

🔐 Auth systems (JWT, OAuth, OTP)

💼 Building complete SaaS & eCommerce solutions

📫 Let’s connect and build something great: LinkedIn | Email

🪪 License
This project is open-source under the MIT License.


---

✅ **Next Steps for You:**
1. Replace `your-username`, `your-repo-name`, `your-profile`, and email with your actual links.
2. Add a live demo link or screenshots if available.
3. Let me know if you want this project to include user login, wishlist, cart, etc., to make it more impressive.

Would you like me to write the **frontend filtering UI code** as well using Shadcn and Tailwind?

