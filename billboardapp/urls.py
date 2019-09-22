from django.contrib import admin
from django.urls import path, include
from billboardapp.views import *


app_name = 'product'

urlpatterns = [
    path('product/create/', ProductCreateView.as_view()),
    path('all/', ProductListView.as_view()),
    path('product/detail/<int:pk>', ProductDetailView.as_view()),
]
