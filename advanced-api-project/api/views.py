from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from rest_framework.exceptions import ValidationError

#List all the books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # anyone can view

#Retrive a single book
class BookDetailView(generics.RetriveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] # anyone can view

#Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # only logged in users

    def perform_create(self, serializer):
        publication_year = self.request.data.get("publication_year")
        if publication_year and int(publication_year) > datetime.now().year:
            raise ValidationError({"publication_year": "Year cannot be in the future."})
        serializer.save()

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # only logged in users

    def perform_update(self, serializer):
        publication_year = self.request.data.get("publication_year")
        if publication_year and int(publication_year) > datetime.now().year:
            raise ValidationError({"publication_year": "Year cannot be in the future."})
        serializer.save()

#Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged in users