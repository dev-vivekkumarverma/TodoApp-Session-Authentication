from django.shortcuts import render
from rest_framework.response import Response
from .models import TodoTask
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TaskSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.



class taskViewSet(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=User.objects.get(username=self.request.user)
        allData=TodoTask.objects.filter(createdBy=user)
        SerialisedData=TaskSerializer(allData,many=True)
        return Response(SerialisedData.data,status=status.HTTP_200_OK)
    

    def post(self,request):

        user=User.objects.get(username=self.request.user)
        request.data['createdBy']=user.pk #externally adding the user.pk to the foreignkey [here reques.data is a dict]
        DeserializedData=TaskSerializer(data=request.data)
        # DeserializedData['createdBy']=user.pk
        try:
            if DeserializedData.is_valid():
                DeserializedData.save()
                return Response(DeserializedData.data,status=status.HTTP_201_CREATED)
            else:
                return Response({'error':"Invalid data passed"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    
    
class taskSearchView(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,onDate:str):
        user=User.objects.get(username=self.request.user)
        allData=TodoTask.objects.filter(createdBy=user,createdOn=onDate)
        SerialisedData=TaskSerializer(allData,many=True)
        return Response(SerialisedData.data,status=status.HTTP_200_OK)
    
    # 15/03/2023
    # Update Api
class taskUpdateView(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    def patch(self, request,id:int):
        user=User.objects.get(username=request.user)
        try:
            taskData=TodoTask.objects.get(id=id,createdBy=user.pk)  
            taskSerializedData=TaskSerializer(taskData,data=request.data,partial=True)
            if taskSerializedData.is_valid():
                taskSerializedData.save()
                return Response(taskSerializedData.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"erroe":"Serializer Validation failed !"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e))
    
        


    # Delete Api
    def delete(self,request,id:int):
        try:
            user=User.objects.get(username=request.user)
            taskData=TodoTask.objects.get(id=id,createdBy=user.pk)
            taskData.delete()
            return Response({'message':"data has been successfully removed !"},status= status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)




