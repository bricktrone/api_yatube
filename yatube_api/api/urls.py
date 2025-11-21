# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

# Создаём роутер для автоматической маршрутизации
v1_router = DefaultRouter()

# Регистрируем вьюсеты
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
# Для комментариев маршрут регистрируется с указанием post_id
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    # Все маршруты из роутера будут доступны по префиксу v1/
    path('v1/', include(v1_router.urls)),
]
