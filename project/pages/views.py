from django.shortcuts import render
from .models import Student

def home_page_view(request):
    student = Student.objects.first()  # جلب أول طالب مدخل في القاعدة
    context = {'student': student}
    return render(request, 'pages/home.html', context)