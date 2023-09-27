from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("all_property/", include("all_property.urls")),
    path("dashboard/", include("dashboard.urls")),
]
