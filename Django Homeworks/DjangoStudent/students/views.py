from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
# Create your views here.
def student_list(request):
    students = Student.objects.all()
    context = {
        'objects' : students
    }
    return render(request, 'students/index.html', context)