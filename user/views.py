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
        return Response(serialized_users.data)  # Use `.data`

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewWithIds(APIView):
    
    def get_object(self,id):   
        try:
            usr = UserModel.objects.get(pk=id)
            return usr
        except UserModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request, id):
        usr = self.get_object(id)
        serializer = UserSerializer(usr)
        return Response(serializer.data)
    
    