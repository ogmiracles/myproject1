from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact']
    }

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = {
        'id': ['exact'],
        'price': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'title': ['exact'],
        'category': ['exact']
    }
    ordering_fields = ['title', 'price']
    ordering = ['title']
    search_fields = ['title']