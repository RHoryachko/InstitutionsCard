from rest_framework import serializers
from .models import Establishment, Comment

class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['establishment', 'text', 'rating', 'author']
        read_only_fields = ['author', 'establishment']

    def validate_establishment(self, value):
        # Впевніться, що заклад існує
        if not value:
            raise serializers.ValidationError("Заклад не знайдено.")
        return value

    def validate_author(self, value):
        # Впевніться, що автор існує
        if not value:
            raise serializers.ValidationError("Автор не знайдений.")
        return value