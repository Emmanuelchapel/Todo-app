from rest_framework import serializers
from .models import Category


# seriazer for the task modal
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','created_at']

        # methode to validate due date
        # def validate_due_date(self, value):
        #     # check if the due date is less thaen the current date
        #     if value and value < date.today():
        #         raise serializers.ValidationError('the due date can not be in the past')
        #     return value



