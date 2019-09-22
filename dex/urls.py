from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

from rest_framework import routers
from billboardapp.views import UserViewSet

# from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register('users', UserViewSet)


# schema_view = get_swagger_view(title='test swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', schema_view),
    path('', include(router.urls)),
    path('api/billboard/', include('billboardapp.urls')),
    path('accounts/', include('rest_framework.urls')),

]