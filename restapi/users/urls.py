from django.contrib import admin
from django.urls import path
# Add include to the import statement here 
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('showusers/', views.allusers, name='allusers'),
    path('profile/', views.profile, name='profile'),
    #view profile using a primary key
    path('profile/<int:pk>/', views.view_profile_pk, name='view_profile_pk'),
    path('dElEtE/', views.delete_all_users, name='delete_all_users'),
    path('dElEtE/<int:pk>/', views.delete_user_pk, name='delete_user_pk'),
]