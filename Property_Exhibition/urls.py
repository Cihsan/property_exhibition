from django.contrib import admin
from django.urls import path,include
from . import views 
from django.views.generic import TemplateView
from accounts import templates


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')), 
     
     
    path('',views.home, name='home'),
    path("", include("accounts.urls")),
    path("all_property/", include("all_property.urls")),
    path("dashboard/", include("dashboard.urls")),
]
