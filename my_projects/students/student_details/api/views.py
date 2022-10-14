from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializer import StudentSerializer
from api.models import Student

# Create your views here.

class StudentView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Student.objects.all()
        serializer=StudentSerializer(qs,many=True)
        return Response(data=serializer.data)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        serializer=StudentSerializer(qs)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        serializer=StudentSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        qs.delete()
        return Response({"message":"student deleted"})





