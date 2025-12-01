from django.urls import path
from . import views
from .models import ScribblePointInfo

urlpatterns = [
    path('', views.index),
    path('<str:extra_input>/', views.detail, name='detail'),
]
