from billboardapp.models import User
from rest_framework.response import Response
from billboardapp.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from billboardapp.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics
from billboardapp.serializers import ProductDetailSerializers, ProductListalizers
from billboardapp.models import Product
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.

# class ProductListViewSchema(AutoSchema):
#     def get_manual_fields(self, path, method):
#         extra_fields = []
#         if method.lower() in ['post', 'put']:
#             extra_fields = [
#                 coreapi.Field('name', 'description', 'price', )
#             ]
#         manual_fields = super().get_manual_fields(path, method)
#         return manual_fields + extra_fields
# #
#
#


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'username', 'first_name', 'last_name', 'email']

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]



class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializers
    permission_classes = [IsLoggedInUserOrAdmin]


class ProductListView(generics.ListAPIView):
    # schema = ProductListViewSchema()
    serializer_class = ProductListalizers
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    # schema = ProductListViewSchema()

    serializer_class = ProductDetailSerializers
    queryset = Product.objects.all()

    permission_classes = [IsLoggedInUserOrAdmin]


