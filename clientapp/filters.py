from django_filters.rest_framework import FilterSet, filters

from clientapp.models import Client
from django.contrib.gis.measure import Distance


class ClientListFilter(FilterSet):
    distance_km = filters.CharFilter(method='filter_list_users_distance', label='Диапазон')

    class Meta:
        model = Client
        fields = ['distance_km', 'sex', 'last_name', 'first_name']

    def filter_list_users_distance(self, queryset, name, distance):
        return queryset.filter(location__distance_lt=(self.request.user.location, Distance(km=distance)))
