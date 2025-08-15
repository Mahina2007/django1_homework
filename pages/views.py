from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home.html')

def hobbies_page(request):
    return render(request, 'hobbies.html')

def my_teachers_page(request):
    return render(request, 'teachers.html')
