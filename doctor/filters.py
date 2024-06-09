from django_filters.rest_framework import FilterSet
from .models import Doctor


class ProductFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'education': ['exact'],
            'hospital': ['exact'],
            'specialty': ['exact'],
        }
