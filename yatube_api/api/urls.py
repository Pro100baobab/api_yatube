from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='post-comments'),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='post-comment-detail'),
]
