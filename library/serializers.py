from rest_framework import serializers

from library.models import Books, Author


class BookSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=255)
    # isbn = serializers.CharField(max_length=255)
    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail')

    class Meta:
        model = Books
        fields = ['title', 'summary', 'isbn', 'genre']


class AuthorSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=255)
    # isbn = serializers.CharField(max_length=255)

    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
