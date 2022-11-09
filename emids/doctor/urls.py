from django.urls import path

from . import views

urlpatterns = [
    path("", views.dash, name="dash_doctor"),
    path("patient/<str:patient_id>", views.patient_profile, name="patient_profile"),
    path("search/<str:patient_id>", views.search, name="search"),

]
 