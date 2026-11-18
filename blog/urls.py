from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]