from rest_framework import serializers
from models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields and validates publication_year.
    """

    class Meta: 
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        """
        Ensure publication year is not in the future.
        """

        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
        """
        Serializes Author model with a nested list of books.
        """
        book = BookSerializer(many=True, read_only=True) # from related_name='books'

        class Meta: 
             model = Author
             fields = ['id', 'name', 'books']