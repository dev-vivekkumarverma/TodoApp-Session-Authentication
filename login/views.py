from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serialiser import UserSerialiser
# Create your views here.


class AuthenticationView(APIView):
    
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        print(self.request.user)
        if self.request.user:
            return redirect(to='todo/')  
        else:
            return redirect(to='auth/login/')
        
    
            


class LoginView(APIView):
    def post(self,request):
        UserSerialisedData=UserSerialiser(data= request.body)
        print(request.body)
        try:
            if UserSerialisedData.is_valid():
                print("hi")
                UserSerialisedData.create()
                print("save")
                return Response(UserSerialisedData.data,status=status.HTTP_201_CREATED)
            else:
                return Response("Error occured")
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    

