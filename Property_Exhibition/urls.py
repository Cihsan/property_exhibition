from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# for api
from rest_framework import routers
from dashboard.views import TestimonialViewSet, PromotionViewSet, FavouriteViewSet
from all_property.views import PropertyViewSet
from accounts.views import (
    LoginAPIView,
    RegistrationAPIView,
    UserLogout,
    UserProfileViewSet,
)

# all user
from accounts.views import AllUsersListView, AllUserDetailView

router = routers.DefaultRouter()
router.register(r"property", PropertyViewSet)
router.register(r"testimonials", TestimonialViewSet)
router.register(r"promotions", PromotionViewSet)
router.register(r"favourite", FavouriteViewSet)
router.register(r"users", UserProfileViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls")),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("logout", UserLogout.as_view(), name="logout"),
    # all api
    path("", include(router.urls)),
    # all user
    path("alluser", AllUsersListView.as_view(), name="alluser"),
    path("alluser/<int:id>/", AllUserDetailView.as_view(), name="alluser_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
