from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.propertylist,name='property'),
    # path('test/', views.Test,name='test'),
    # path('detail_property/<int:pk>', views.propertyDetail.as_view(), name='detail_property'),
    # path('search/', views.search.as_view(), name='search-view'),   
]