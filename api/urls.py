
from rest_framework.routers import DefaultRouter
from users.views import UserViewSets
from posts.views import PostViewSet
from comments.views import CommentViewSet
from post_reactions.views import LikeViewSet
from post_reactions.views import DislikeViewSet
from followers.views import FollowViewSet
from user_profile.views import ProfileViewSet
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router=DefaultRouter()

urlpatterns=[
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

router.register(r'users',UserViewSets,basename='users')
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'like',LikeViewSet)
router.register(r'Dislike',DislikeViewSet)

router.register(r'follow',FollowViewSet)

router.register(r'profiles',ProfileViewSet)


urlpatterns=urlpatterns+router.urls
