from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from billboardapp.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from billboardapp.serializers import UserSerializer, ProductDetailSerializers, ProductListSerializers
from billboardapp.models import User, Product
from billboardapp.paginations import StandardResultsSetPagination
from rest_framework.filters import SearchFilter, OrderingFilter



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'first_name', 'last_name', 'email']

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializers
    permission_classes = (IsAuthenticated, )


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializers
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializers
    queryset = Product.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )