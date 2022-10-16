from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('checking/', views.index, name='checking'),
    path('login/', CustomLoginView.as_view(),name='login'),
    path('logout/', logoutUser,name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    ]