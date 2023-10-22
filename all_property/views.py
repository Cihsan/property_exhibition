from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response

# for api
from rest_framework import viewsets
from .models import Property, Property_Images
from .serializers import PropertySerializer
from django.db.models import Prefetch
from dashboard.models import Promotion


# property api
from rest_framework import viewsets, generics, views
from .models import Property
from .serializers import PropertySerializer, PropertyImagesCreateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["name", "description"]

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


class PropertyImagesCreateView(views.APIView):
    def post(self, request):
        property_id = request.data.get("property_id")
        try:
            property = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response(
                {"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PropertyImagesCreateSerializer(data=request.data)

        if serializer.is_valid():
            image_urls = serializer.validated_data.get("urls", [])
            for url in image_urls:
                Property_Images.objects.create(property_id=property, url=url)
            return Response(
                {"message": "Images added successfully"}, status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
