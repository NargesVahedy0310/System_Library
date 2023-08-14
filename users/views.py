from rest_framework import viewsets
from .models import CreateUser, BorrowedBook
from .serializers import CreateUserSerializer, BorrowedBookSerializer

class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = CreateUser.objects.all()
    serializer_class = CreateUserSerializer

class BorrowedBookViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer
