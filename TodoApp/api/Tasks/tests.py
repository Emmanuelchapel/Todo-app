from django.test import TestCase
from api.Categories.models import Category
from .models import Tasks
from .serializer import TaskSerializer


class TaskSerializerTests(TestCase):
    def test_task_serializer_accepts_category_id_for_create(self):
        category = Category.objects.create(name='Work')

        payload = {
            'task': 'Write report',
            'category': category.id,
            'priority': 'MEDIUM',
            'due_date': '2026-09-15',
        }

        serializer = TaskSerializer(data=payload)

        self.assertTrue(serializer.is_valid(), serializer.errors)
        task = serializer.save()
        self.assertEqual(task.category_id, category.id)
        self.assertEqual(task.task, 'Write report')
        self.assertEqual(task.priority, 'MEDIUM')
