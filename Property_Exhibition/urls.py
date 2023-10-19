from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# for api
from rest_framework import routers
from dashboard.views import (
    TestimonialViewSet,
    PromotionViewSet,
    FavouriteViewSet,
    BookingsViewSet,
    payment_view,
    complete_transaction,
    cancel_transaction,
)
from all_property.views import PropertyViewSet
from accounts.views import (
    LoginAPIView,
    RegistrationAPIView,
    LogoutView,
    UserProfileViewSet,
    DeleteUserView,
)


# all user
from accounts.views import AllUsersListView, AllUserDetailView

router = routers.DefaultRouter()
router.register(r"property", PropertyViewSet)
router.register(r"testimonials", TestimonialViewSet)
router.register(r"promotions", PromotionViewSet)
router.register(r"favourite", FavouriteViewSet)
router.register(r"users", UserProfileViewSet, basename="users")
router.register(r"bookings", BookingsViewSet, basename="bookings")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls")),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    # all api
    path("", include(router.urls)),
    # all user
    path("alluser", AllUsersListView.as_view(), name="alluser"),
    path("alluser/<int:id>/", AllUserDetailView.as_view(), name="alluser_detail"),
    path("alluser/delete/<int:id>", DeleteUserView.as_view(), name="user_delete"),
    path("payment/", payment_view, name="payment"),
    path("success/<str:tran_id>", complete_transaction, name="complete_transaction"),
    path("cancel/<str:tran_id>", cancel_transaction, name="cancel_transaction"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
