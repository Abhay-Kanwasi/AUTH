from django.urls import path
from account import views

urlpatterns = [
    path('', views.index)
#     path('register/', views.UserRegisterationView.as_view(), name='register'),
#     path('login/', views.UserLoginView.as_view(), name='login'),
#     path('profile/', views.UserProfileView.as_view(), name='profile'),
#     path('change_password/', views.UserChangePasswordView.as_view(), name='change_password'),
#     path('send_password_reset_email/', views.SendPasswordResetEmailView.as_view(), name='send_password_reset_email'),
#     path('rest_password_email/<uid>/<token>/', views.ResetPasswordEmailView.as_view(), name='reset_password_email')
]

