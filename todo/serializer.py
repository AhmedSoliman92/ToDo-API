from rest_framework import serializers
from todo.models import Todo


class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_completed',)
