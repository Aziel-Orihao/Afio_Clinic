from django.urls import path
from . import views  # import the views from this app

urlpatterns = [
    path('', views.home, name='home'),  # root URL goes to the home view
]

path('patients/', views.patient_list, name='patient_list'),
