from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change-password',views.change_password,name='change-password'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api_token_auth'),
]
