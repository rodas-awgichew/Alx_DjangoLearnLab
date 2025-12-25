from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns += [
    path('posts/<int:pk>/like/', LikePostView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view()),
]