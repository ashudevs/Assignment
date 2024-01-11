from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .forms import *
from .serializers import *
from rest_framework import status

@api_view(['GET'])
def FirstTask(request):
    try:
        a = 'Hello World'
        return Response({a})
    except Exception as e:
        return Response({'error': str(e)})
    

@api_view(['GET'])
def SecondTask(request):
    try:
        all_users = users.objects.all()
        return render(request, 'app/index.html', {'users': all_users})
    except Exception as e:
        return Response({'error': str(e)})
    

@api_view(['GET'])
def ThirdTask(request):
    try:
        return render(request, 'app/new_user.html')
    except Exception as e:
        return Response({'error': str(e)})
@api_view(['POST'])
def ThirdTash1(request):
    try:
        serializer = userdbserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)})
    
    
    
@api_view(['GET'])
def ForthTask(request, id):
    try:
        if not id:
            return Response({'error': 'Please provide the user ID in the URL.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = users.objects.get(id=id)
        except users.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = userdbserializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)})