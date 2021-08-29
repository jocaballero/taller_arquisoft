from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('list/<str:id>/', views.get_measurements_id, name='measurementId')
]