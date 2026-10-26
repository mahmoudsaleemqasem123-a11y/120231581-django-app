from django.shortcuts import render
from .models import Student

def home_page_view(request):
    # جلب أول طالب تم إدخال بياناته من لوحة المشرف
    student = Student.objects.first()
    context = {'student': student}
    return render(request, 'pages/home.html', context)