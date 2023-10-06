from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# for api
from rest_framework import routers
from all_property.views import PropertyViewSet
from dashboard.views import TestimonialReadOnlyViewSet, PromotionReadOnlyViewSet

router = routers.DefaultRouter()
router.register(r"properties", PropertyViewSet)
router.register(r"testimonials", TestimonialReadOnlyViewSet)
router.register(r"promotions", PromotionReadOnlyViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("", include("accounts.urls")),
    path("all_property/", include("all_property.urls")),
    path("dashboard/", include("dashboard.urls")),
    # all api
    path("api/", include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
