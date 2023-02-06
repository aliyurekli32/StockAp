from django.urls import path
from rest_framework import routers
from .views import CategoryMVS,BrandView,FirmView,ProductView,PurchaseView,SalesView

router = routers.DefaultRouter()

router.register("categories", CategoryMVS)
router.register("brands", BrandView)
router.register("firms", FirmView)
router.register("products", ProductView)
router.register("purchases", PurchaseView)
router.register("sales", SalesView)

urlpatterns = [
    
] + router.urls
