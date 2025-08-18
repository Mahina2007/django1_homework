from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def my_contacts_page(request):
    context = {}
    return render(request, 'contacts.html', context)
