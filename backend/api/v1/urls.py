from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('api_schema', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
    ), name='swagger-ui'),
    path('categories/', include('categories.Presentation.CategoryUrls')),
    path('products/', include('products.Presentation.ProductUrls')),
    path('cart/', include('shopping_cart.Presentation.CartUrls')),
    path('cartitem/', include('shopping_cart.Presentation.CartItemUrls')),
]


