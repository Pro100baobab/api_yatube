from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

# Роутер для версии v1 API
router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='v1-posts')
router_v1.register(r'groups', GroupViewSet, basename='v1-groups')
router_v1.register(
    r'posts/(?P<post_pk>\d+)/comments',
    CommentViewSet,
    basename='v1-post-comments'
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
