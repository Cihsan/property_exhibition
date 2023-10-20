from django.shortcuts import render, HttpResponse

# for api
from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from django.db.models import Prefetch
from dashboard.models import Promotion


# Create your views here.
def propertylist(request):
    return render(request, "property.html")


# property api
from rest_framework import viewsets, generics
from .models import Property
from .serializers import PropertySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["name", "description", "other_fields_to_search"]

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.query_params.get("sort_by")
        if sort_by == "min_price":
            queryset = queryset.order_by("price_field")
        elif sort_by == "max_price":
            queryset = queryset.order_by("-price_field")
        elif sort_by == "a_to_z":
            queryset = queryset.order_by("name_field")
        elif sort_by == "z_to_a":
            queryset = queryset.order_by("-name_field")
        elif sort_by == "min_area":
            queryset = queryset.order_by("area_field")
        elif sort_by == "max_area":
            queryset = queryset.order_by("-area_field")

        return queryset
