from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Clarusway StockApp API",
        default_version="v1",
        description="Clarusway StockApp API",
        terms_of_service="#",
        # Change e-mail on this line!
        contact=openapi.Contact(email="anthonyharold67@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),
    path('stock/', include("stock.urls")),


    path("swagger(<format>\.json|\.yaml)",
         schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schemaredoc"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)