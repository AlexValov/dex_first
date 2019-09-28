from django.urls import path
from billboardapp.views import *


urlpatterns = [
    path('products/create/', ProductCreateView.as_view()),
    path('products/all/', ProductListView.as_view()),
    path('products/detail/<int:pk>', ProductDetailView.as_view()),
]