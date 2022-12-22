from django.shortcuts import render
from .models import Book
from .serializer import bookserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
class BookList(APIView):
    def get(self,request):
        try:
            books=Book.objects.all()
        except:
            return Response({"error:Books list doesn't exist"},status=HTTP_404_NOT_FOUND)
        serialize=bookserializer(books,many=True)
        return Response(serialize.data)
class BookCreate(APIView):
    def post(self,request):
        serialize=bookserializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
class SelectedBook(APIView):
    def get(self,request,id):
        try:
            book =Book.objects.values().get(id=id)
        except:
            return Response({"error:Book doesn't exist"},status=HTTP_404_NOT_FOUND)
        serialize=bookserializer(book)
        return Response(serialize.data)
    def put(self,request,id):
        try:
            book =Book.objects.all().get(id=id)
        except:
            return Response({"error:Book doesn't exist"},status=HTTP_404_NOT_FOUND)
        serialize=bookserializer(book,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
    def delete(self,request,id):
        try:
            book =Book.objects.values().get(id=id)
        except:
            return Response({"error:Book doesn't exist"},status=HTTP_404_NOT_FOUND)
        book.delete()
        return Response("BOOK WAS DELETED")

