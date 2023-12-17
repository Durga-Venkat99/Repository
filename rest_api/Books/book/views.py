from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# READ
@api_view(['GET'])
def booklist(request):
    booksobj =  bookmodel.objects.all()               # query set
    serializer = BookSerializer(booksobj,many=True)   # passing all query set in booksobj
    return Response(serializer.data)

# CREATE
@api_view(['POST'])
def post_book(request):
    bookobj = bookmodel.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# UPDATE
@api_view(['POST'])
def update_book(request,id):
    bookobj = bookmodel.objects.get(id = id)
    serializer = BookSerializer(instance=bookobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# DELETE
@api_view(['DELETE'])
def delete_book(request,id):
    bookobj = bookmodel.objects.get(id = id)
    bookobj.delete()
    return Response("book is delete")