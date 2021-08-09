from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
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