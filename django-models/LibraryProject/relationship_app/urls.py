from django.urls import path
from .views import list_books, LibraryDetailView, register, login, logout

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('', list_books, name='list_books'), # CBV (you might want to rename this if actually class-based)
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
