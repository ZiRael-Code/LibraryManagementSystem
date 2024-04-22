import segno
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from library.models import Books, Author
from library.serializers import BookSerializer, AuthorSerializer


# Create your views here.

# @api_view(['GET', 'POST'])


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GenericBookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    # def get_queryset(self):
    #     return Books.objects.all()


class GenericBookDetail(RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()


class GenericAuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GenericAuthorDetail(RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookList(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True,
                                    context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetails(APIView):
    # @api_view(['GET', 'PUT', 'DELETE'])
    def get(self, request, id):
        book = get_object_or_404(Books, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        book = get_object_or_404(Books, pk=id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        book = get_object_or_404(Books, pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class Author
# @api_view(['GET', 'POST', 'PUT'])
class CreateList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
class AuthorDetails(APIView):
    def get(self, request, id):
        author = get_object_or_404(Author, pk=id)
        serializer = AuthorSerializer(author)
        author_qrcode = segno.make_qr("Welcome to Django")
        author_qrcode.save("qrcode.png")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        author = get_object_or_404(Author, pk=id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        author = get_object_or_404(Author, pk=id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
