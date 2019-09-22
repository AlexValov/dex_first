from django.urls import path
from billboardapp.views import *

app_name = 'product'

urlpatterns = [
    path('product/create/', ProductCreateView.as_view()),
    path('product/all/', ProductListView.as_view()),
    path('product/detail/<int:pk>', ProductDetailView.as_view()),
]
