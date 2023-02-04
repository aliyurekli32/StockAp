from django.urls import path
from rest_framework import routers
from .views import CategoryMVS,BrandView

router = routers.DefaultRouter()
router.register("categories", CategoryMVS)
router.register("brands", BrandView)

urlpatterns = [
    
] + router.urls
