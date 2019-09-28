from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from billboardapp.views import UserViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register('users', UserViewSet)

schema_view = get_swagger_view(title='DEX_test')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_framework.urls')),
    path('api/v1/auth/', include(router.urls)),
    path('api/v1/billboardapp/', include('billboardapp.urls')),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]