from rest_framework import serializers
from .models import CreateUser, BorrowedBook

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUser
        fields = ['id', 'username', 'first_name', 'last_name']

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['id', 'user', 'book', 'borrowed_at', 'returned_at']
