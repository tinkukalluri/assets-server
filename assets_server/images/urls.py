from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view()),
    path('asset_images', views.asset_images.as_view())
]
