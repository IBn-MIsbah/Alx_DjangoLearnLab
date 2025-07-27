from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('', views.list_books, name='list_books'), # CBV
]
