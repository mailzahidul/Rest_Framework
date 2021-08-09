from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializers, StudentCreateSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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