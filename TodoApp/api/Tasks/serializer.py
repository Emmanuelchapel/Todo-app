from rest_framework import serializers
from .models import Tasks
from datetime import date
from api.Categories.models import Category
from api.Categories.serializer import CategorySerializer

# seriazer for the task modal
class TaskSerializer(serializers.ModelSerializer):

    due_date = serializers.DateField(
        format="%m/%d/%Y",
        input_formats=["%m/%d/%Y", "iso-8601", "%b-%d-%Y"]
    )

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    Category = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'task', 'category', 'Category', 'priority', 'due_date', 'Done', 'create_at']

    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError('the due date can not be in the past')
        return value



