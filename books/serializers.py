from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'author', 'publication_date', 'page_count', 'language', 'available', 'checked_out_at', 'checked_out_by')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
