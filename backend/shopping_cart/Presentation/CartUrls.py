from .CartDetailView import cart_detail_view 
from django.urls import path

urlpatterns = [
    path('<int:pk>/product-list', cart_detail_view),
]