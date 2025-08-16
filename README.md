# KHAMPHA RESTUARANT

A Django-based web application for managing a restaurant menu, shopping cart, and order history. Users can browse menu items, add them to a cart, place orders, and view their order history. Authentication is provided for user signup and login.

## Features

- User registration and authentication
- Menu browsing by category
- Add/remove menu items to/from shopping cart
- Place orders and view order history
- Responsive UI with Tailwind CSS
- Admin interface for managing menu items and categories

## Project Structure

```
restuarant_project/
├── db.sqlite3
├── manage.py
├── menu/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── menu_images/
│   └── [menu item images]
├── restuarant_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates/
    ├── base.html
    ├── menu/
    │   ├── cart.html
    │   ├── menu_list.html
    │   └── order_history.html
    └── registration/
        ├── login.html
        └── signup.html
```

## Setup Instructions

1. **Clone the repository**  
   ```
   git clone <repo-url>
   cd restuarant_project
   ```

2. **Create and activate a virtual environment**  
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**  
   ```
   pip install django
   ```

4. **Apply migrations**  
   ```
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**  
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**  
   ```
   python manage.py runserver
   ```

7. **Access the application**  
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Browse the menu and add items to your cart.
- View your cart and place orders.
- Register or log in to view your order history.
- Admins can manage menu items and categories at `/admin/`.

## License

This project is for educational purposes.

