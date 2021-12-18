from django.contrib import admin
from django.urls import path
from . import views  # . 은 같은 디렉토리 안에서 가져온다는걸 의미

urlpatterns = [
    path('index/', views.index)
]
