from django.urls import path

from python_web_framework_project.blogs import views

urlpatterns = (
    path('', views.BlogListView.as_view(), name='index'),
    path('<int:pk>/', views.BlogDetailsView.as_view(), name='blog details'),
    path('<int:pk>/<slug:slug>/', views.BlogDetailsView.as_view(), name='blog details'),
    path('create/', views.CreateBlogView.as_view, name='create blog'),
)
