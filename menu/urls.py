from django.urls import path
from .views import (
    MenuListView, 
    AddToCartView, 
    CartView, 
    RemoveFromCartView,
    PlaceOrderView,
    OrderHistoryView,
    SignupView,
)

urlpatterns = [
    # Menu and Cart
    path('', MenuListView.as_view(), name='menu_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),

    # Order
    path('place-order/', PlaceOrderView.as_view(), name='place_order'),
    path('order-history/', OrderHistoryView.as_view(), name='order_history'),
    
    # Auth
    path('signup/', SignupView.as_view(), name='signup'),
]
