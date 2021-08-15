from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializers, StudentCreateSerializer, StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

def student_info(request, id):
    stu = Student.objects.get(id=id)
    python_data = StudentSerializers(stu)   				            # convert obj_instance to python data
    # json_data = JSONRenderer().render(python_data.data)               # convert python data to json data    python_data.data makes python data to dict          
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(python_data.data)          			            # We can merge line no. 12 and 13 with 14
 
 
def student_info_list(request):
    stu = Student.objects.all()
    python_data = StudentSerializers(stu, many=True)                    # convert obj_instance to python data
    json_data = JSONRenderer().render(python_data.data)                 # convert python data to json data
    print(json_data)                                                    # python_data.data makes python data to dictionary
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(python_data.data, safe=True)		            # We can merge line no. 12 and 13 with 14

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data, "request body")
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentCreateSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'success'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')
        msg = {'msg':'failed'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type = 'application/json')


@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def function_base_view(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializers(student)
            return Response(serializer.data, status = status.HTTP_200_OK)

        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)          # request.data works like request.POST
        if serializer.is_valid():
            name = serializer.validated_data['name']
            roll = serializer.validated_data['roll']
            city = serializer.validated_data['city']
            obj = Student.objects.create(name=name, roll=roll, city=city)
            return Response({'staus':'Ok'}, status = status.HTTP_200_OK)
        else:
            return Response(py_data.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':                                     # PUT Work for Complete Upsata an object data
        id=pk
        student = Student.objects.get(id=pk)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            roll = serializer.validated_data['roll']
            city = serializer.validated_data['city']
            student.name = name
            student.roll = roll
            student.city = city
            student.save()
            return Response({'msg':"Complete Update successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id=pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg':'Student Deleted !!!'}, status=status.HTTP_200_OK)


class ClassBaseView(APIView):
    def get(self, request, pk=None, format = None):
        id = pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer = StudentModelSerializer(stu)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            stu=Student.objects.all()
            serializer = StudentModelSerializer(stu, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    def post(self, request, format = None):
        serializer = StudentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student Create Successfully...'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None, format = None):             # put work for Partial Update 
        id=pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentModelSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Put work successfully...'}, status= status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk, format = None):                    # patch work for Partial Update 
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer= StudentModelSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'mgs':'Path work successfully...'}, status= status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format = None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Delete Successfully..'}, status = status.HTTP_200_OK)

