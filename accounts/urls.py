from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name = 'register'), 
    path('', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('password_change/', views.MyPasswordChangeView.as_view(), name = 'password-change'),
    path('password_change_done/', views.MyPasswordChangeDoneView.as_view(), name = 'password-change-done'),
]