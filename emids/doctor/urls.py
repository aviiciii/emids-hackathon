from django.urls import path

from . import views

urlspatterns = [
    path("", views.dash, name="doc_dash"),  
     
]
 