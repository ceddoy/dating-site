from django_filters.rest_framework import FilterSet

from clientapp.models import Client


class ClientListFilter(FilterSet):

    class Meta:
        model = Client
        fields = ['sex', 'last_name', 'first_name']
