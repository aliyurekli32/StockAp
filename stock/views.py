from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Brand,Category,Firm,Product,Purchases,Sales
from .serializers import CategorySerializer,CategoryProductSerializer,BrandSerializer
from django_filters import rest_framework as filtera
from rest_framework.permissions import DjangoModelPermissions



# Create your views here.

class CategoryMVS(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends =[filters.SearchFilter, filtera.DjangoFilterBackend]
    search_fields=["name",]
    filterset_fields = ["name",]
    permission_classes = [DjangoModelPermissions]
    
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
            return CategoryProductSerializer
        return super().get_serializer_class()
    
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
