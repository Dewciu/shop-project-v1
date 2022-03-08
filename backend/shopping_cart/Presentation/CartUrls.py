from .CartDetailView import cart_detail_view 
from .CartCreateView import cart_create_view
from django.urls import path

urlpatterns = [
    path('', cart_create_view),
    path('<int:pk>/product-list', cart_detail_view),
]