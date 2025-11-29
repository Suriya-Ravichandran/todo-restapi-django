from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['POST'])
def createtodo(request):
    if request.method=='POST':
         serializer = TodoSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def showtodos(request):
    if request.method=='GET':
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getonetodo(request,pk):
    try:    
        todos=Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo Not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=TodoSerializer(todos)
        return Response(serializer.data)

@api_view(['PUT'])
def updatetodo(request,pk):
    try:    
        todos=Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo Not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
         serializer = TodoSerializer(todos,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def deletetodo(request,pk):
    try:    
        todos=Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo Not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        todos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)