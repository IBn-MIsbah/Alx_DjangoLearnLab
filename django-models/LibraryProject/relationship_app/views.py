# from django.shortcuts import render, get_object_or_404
# from .models import Book, Library
# from django.views.generic import DetailView
# from django.views.generic.detail import DetailView

# # Function-based view to list all books
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'library_detail.html'
#     context_object_name = 'library'
from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
