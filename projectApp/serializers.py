from rest_framework import serializers

from projectApp.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  )
