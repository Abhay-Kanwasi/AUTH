from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.UserRegisterationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('change_password/', views.UserChangePasswordView.as_view(), name='change_password')
]

