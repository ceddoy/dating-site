from django_filters.rest_framework import FilterSet, filters

from clientapp.models import Client, Location
from django.contrib.gis.measure import Distance


class ClientListFilter(FilterSet):
    distance_km = filters.CharFilter(method='filter_list_users_distance', label='Диапазон')

    class Meta:
        model = Client
        fields = ['distance_km', 'sex', 'last_name', 'first_name']

    def filter_list_users_distance(self, queryset, name, distance):
        locations = Location.objects.all().order_by('-user').distinct('user')

        locations = locations.filter(location__distance_lt=(Location.objects.filter(user=self.request.user).last().location,
                                                            Distance(km=distance))).exclude(user=self.request.user)

        return queryset.filter(id__in=[location.user_id for location in locations])
