from .models import Brand,Category,Firm,Product,Purchases,Sales
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ["id","name","product_count"]
        
    def get_product_count(self,obj):
        return Product.objects.filter(category_id=obj.id).count()
    
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stock",
        )
        read_only_fields = ("stock",)
    
class CategoryProductSerializer(serializers.ModelSerializer):
    c_products = ProductSerializer(many=True)
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ["id","name","product_count","c_products"]
    def get_product_count(self,obj):
        return Product.objects.filter(category_id=obj.id).count()

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "image"
        )