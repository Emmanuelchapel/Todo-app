from django.db import models
from api.Categories.models import Category
from datetime import date

# Create your models here.
class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('lOW', 'low'),
        ('MEDIUM', 'Medium'),
        ('HIGH','High')
    ]
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='Tasks', on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    due_date = models.DateField(default= date.today)
    Done = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task



        