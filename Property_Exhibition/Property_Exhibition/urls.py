from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',views.home, name='home'),
=======
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("all_property/", include("all_property.urls")),
    path("dashboard/", include("dashboard.urls")),
>>>>>>> 064ecd0bac1c4bdc441c1e923a057c16b0653b9f
]
