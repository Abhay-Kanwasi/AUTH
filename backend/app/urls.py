from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.urls import re_path as url
from .views import create_user

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path("api/create_user", create_user, name="create_user"),
]