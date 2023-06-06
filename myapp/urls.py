from django.urls import path
from .views import about, login, contacts, add_form, index_myapp

urlpatterns = [
    path('', index_myapp),
    path('about/', about),
    path('login/', login),
    path('contacts/<str:id>/', contacts),
    path('add_form/', add_form, name='add_form')

]