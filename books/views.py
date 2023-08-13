from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class CreateBook(ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def create(self, request, *args, **kwargs):
        # داده‌های ارسالی از درخواست استخراج می‌شوند
        data = request.data

        # بررسی اعتبار داده‌های ارسالی
        if not data.get('title') or not data.get('author') or not data.get('publication_date'):
            # اگر داده‌های ارسالی ناکافی باشد، پاسخ با کد خطا ۴۰۰ برگردانده می‌شود
            return Response({'detail': 'Invalid data. Make sure title, author, and publication_date are provided.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # اعتبار داده‌ها بررسی شد، داده جدید ایجاد می‌شود
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # پاسخ مناسبی برای کاربر ارسال می‌شود
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookId(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)