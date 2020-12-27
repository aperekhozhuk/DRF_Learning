from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.api_overview),
    path('users/', views.UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),
    path('posts/', views.PostList.as_view(), name = 'post-list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name = 'post-detail'),
    path('auth/', include('rest_framework.urls')),
]
