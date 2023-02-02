import django_filters
from django_filters import CharFilter

from app.models import CustomUser


class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',label='',lookup_expr='icontains',)
    class Meta:
        model = CustomUser
        fields = ('name',)