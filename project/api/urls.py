from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet, basename='posts')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'posts', views.PostViewSet, basename='user-posts')
users_router.register(r'comments', views.CommentReadOnlyViewSet, basename='user-comments')

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', views.CommentViewSet, basename='post-comments')

user_posts_router = routers.NestedSimpleRouter(
    users_router,
    r'posts',
    lookup='post'
)
user_posts_router.register(
    r'comments',
    views.CommentViewSet,
    basename='user-post-comments'
)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(users_router.urls)),
    path('', include(posts_router.urls)),
    path('', include(user_posts_router.urls)),
    path('auth/', include('rest_framework.urls')),
]
