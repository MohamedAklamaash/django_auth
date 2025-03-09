from django.urls import path
from .views import BooksView, BooksDetailView

urlpatterns = [
    path('', BooksView.as_view(), name='books-list'),  
    path('<int:id>', BooksDetailView.as_view(), name='books-detail'),
]
