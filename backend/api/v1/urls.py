from django.urls import path, include

urlpatterns = [
    path('categories/', include('products.Presentation.urls')),
]
