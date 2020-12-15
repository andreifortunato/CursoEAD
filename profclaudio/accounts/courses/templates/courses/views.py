from django.shortcuts import render

from .models import Course

def index(request):
    courses = Course.objects.all()
    template_name = 'courses/courses.html'
    context = {
        'courses' : courses
    }
    return render(request, template_name)

