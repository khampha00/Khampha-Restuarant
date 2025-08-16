#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, MenuItem, Order, OrderItem
from django.db.models import F, Sum

# --- User Authentication Views ---

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu_list')
        return render(request, 'registration/signup.html', {'form': form})

# --- Core Application Views ---

class MenuListView(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('menu_items').all()
        return render(request, 'menu/menu_list.html', {'categories': categories})

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        menu_item = get_object_or_404(MenuItem, id=item_id)
        cart = request.session.get('cart', {})
        
        cart_item = cart.get(str(item_id))
        if cart_item:
            cart_item['quantity'] += 1
        else:
            cart[str(item_id)] = {'name': menu_item.name, 'price': str(menu_item.price), 'quantity': 1}
        
        request.session['cart'] = cart
        return redirect('cart')

class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = 0
        
        for item_id, item_data in cart.items():
            total_item_price = float(item_data['price']) * item_data['quantity']
            cart_items.append({
                'id': item_id,
                'name': item_data['name'],
                'price': item_data['price'],
                'quantity': item_data['quantity'],
                'total_price': total_item_price,
            })
            total_price += total_item_price
            
        return render(request, 'menu/cart.html', {'cart_items': cart_items, 'total_price': total_price})

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session['cart'] = cart
        return redirect('cart')

class PlaceOrderView(LoginRequiredMixin, View):
    def post(self, request):
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('menu_list') # Redirect if cart is empty

        # Calculate total price on the server-side to ensure accuracy
        total_price = 0
        items_for_order = []
        for item_id, item_data in cart.items():
            menu_item = get_object_or_404(MenuItem, id=int(item_id))
            total_price += menu_item.price * item_data['quantity']
            items_for_order.append({'item': menu_item, 'quantity': item_data['quantity']})

        # Create the order
        order = Order.objects.create(user=request.user, total_price=total_price)

        # Create the order items
        for data in items_for_order:
            OrderItem.objects.create(
                order=order,
                menu_item=data['item'],
                quantity=data['quantity'],
                price=data['item'].price
            )

        # Clear the cart from the session
        del request.session['cart']
        
        return redirect('order_history')

class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user).prefetch_related('items__menu_item').order_by('-created_at')
        return render(request, 'menu/order_history.html', {'orders': orders})

