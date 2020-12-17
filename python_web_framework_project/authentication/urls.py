from django.urls import path

from python_web_framework_project.authentication import views

urlpatterns = (
    path('register/', views.RegisterView.as_view(), name='register'),
    path('log-in/', views.LogInView.as_view(), name='log in'),
    path('log-out/', views.LogOutView.as_view(), name='log out'),
)
