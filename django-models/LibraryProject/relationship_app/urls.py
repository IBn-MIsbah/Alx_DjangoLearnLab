from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('', views.list_books, name='list_books'), # CBV
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
