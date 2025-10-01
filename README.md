# 🔍 Advanced Product Search & Filter System – Full-Stack Portfolio Project

This is a full-stack portfolio project built with **Django REST Framework**, **MySQL**, **Django Unfold**, **Next.js App Router**, **Tailwind CSS**, and **Shadcn UI**. It showcases a robust and scalable **search and filtering system** for products using **django-filter**, dynamic query handling, and a modern, animated frontend.

> ⚡ This project demonstrates my skills as a **Full-Stack Developer**, capable of building optimized APIs, integrating advanced search filters, **pagination**, and designing interactive user interfaces with professional UI libraries.

---

## ✨ Key Features

### 🔧 Backend (Django + DRF + MySQL)

* **Product Filtering** using `django-filter` with custom filters:

  * Category filter
  * Price range (min, max)
  * Product rating
* **Advanced Search** with `SearchFilter` and `OrderingFilter`
* **Pagination** with `PageNumberPagination`:

  * Configurable page size (default: 8 products per page)
  * Seamless integration with the frontend for dynamic page navigation
* **Clean API design** with `ListAPIView`
* **Admin UI customization** using [Django Unfold](https://github.com/md-ajim/django-admin-custom)
* **MySQL** database for relational data and performance

### 💻 Frontend (Next.js App Router + Tailwind CSS + Shadcn UI)

* Fully dynamic frontend using **Next.js App Router**
* **Interactive UI** with **Shadcn UI** components
* Responsive filtering UI for category, price range, and rating
* **Pagination controls** that fetch the correct page of products from the backend and update the UI accordingly
* Live search functionality with debounce
* Mobile-first design with **Tailwind CSS**
* API consumption from DRF with real-time filter and pagination support

---

🚀 How to Run

🛠 Backend Setup

```bash
git clone https://github.com/md-ajim/Advanced-Product-Search-Filter-System.git
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

🌐 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

🧠 Why This Project Matters
This project reflects:

📊 Real-world eCommerce use case

🎯 Precision filtering and pagination logic handled at backend level

🧹 Decoupled architecture with DRF + Next.js

🎨 Modern UI design using industry-standard Shadcn UI and Tailwind CSS

🔄 Live search, filtering, sorting, and pagination powered by a clean REST API

---

👨‍💻 About Me
I’m a results-driven Full-Stack Developer passionate about building high-performance, scalable, and user-centric web applications. I specialize in:

🔗 Next.js, Tailwind, Shadcn UI

🛠 Django REST Framework, MySQL, JWT

🔐 Auth systems (JWT, OAuth, OTP)

💼 Building complete SaaS & eCommerce solutions

📨 Let’s connect and build something great: LinkedIn | Email

---

🪪 License
This project is open-source under the MIT License.

MIT — free to use for reference and learning.

---


