from django.urls import path

from . import views

urlspatterns = [
    path("", views.index, name="doc_dash"),  
    path("")  
]
 