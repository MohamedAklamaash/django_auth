from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserSerializer

class UserView(APIView):
    
    def get(self, request):
        usrs = UserModel.objects.all()
        serialized_users = UserSerializer(usrs, many=True)
        return Response(serialized_users)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(): # username, email, password 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

