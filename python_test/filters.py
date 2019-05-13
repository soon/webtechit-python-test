import django.db.models
import django_filters

from python_test import models


class ClientFilter(django_filters.FilterSet):
    o = django_filters.OrderingFilter(
        fields=(
            'name',
            'email',
            'phone_number',
            'suburb',
        )
    )

    class Meta:
        model = models.Client

        fields = {
            'name',
            'email',
            'phone_number',
            'suburb',
        }
        filter_overrides = {
            django.db.models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            django.db.models.EmailField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
