from django.shortcuts import render
from  rest_framework import viewsets
from .models import Tasks
from .serializer import TaskSerializer
from .filter import TaskFilter

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter

    