from django.views.generic import ListView
from django.shortcuts import render 
from school.models import Teacher , Student 

def student_list(request):
    template = '/school/student_list.html'
    context = {'object_list': Student.objects.order_by('group'),
               'teachers': Teacher.objects.all()}
    ordering = 'group'
    return render (request , template , context)

