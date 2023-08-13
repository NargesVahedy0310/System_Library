from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'books', BookId)

urlpatterns = [
    path('books/', CreateBook.as_view({'get': 'list', 'post': 'create'}), name='create-book'),
    path('', include(router.urls)),
]






