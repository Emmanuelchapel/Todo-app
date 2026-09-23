from os import name

import django_filters
from api.Tasks.models import Tasks

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Tasks
        fields = {'task':['iexact', 'icontains']}