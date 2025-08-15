from django.urls import path


from pages.views import home_page_view, hobbies_page, my_teachers_page

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name = "home" ),
    path('hobbies/', hobbies_page, name = "hobbies" ),
    path('teachers/', my_teachers_page, name = "teachers" ),
]