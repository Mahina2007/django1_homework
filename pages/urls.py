from django.urls import path


from pages.views import home_page_view, about_page, my_contacts_page

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name = "home" ),
    path('about/', about_page, name = "about" ),
    path('contacts/', my_contacts_page, name = "contacts" ),
]