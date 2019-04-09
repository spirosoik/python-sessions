from django.urls import path

from .views import MyView
from . import views

urlpatterns = [
  path('index/', views.index, name='index'),
  path('index/<str:name>/', views.name, name='name'),
  path('template/<str:name>/', views.template, name='template'),
  path('mine/', MyView.as_view(), name='my-view'),
]
