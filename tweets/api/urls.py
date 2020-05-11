from django.urls import path
from .views import (
    TweetListAPIView, 
    TweetDetailAPIView,
    TweetCreateAPIView,
    TweetUpdateAPIView,
    TweetDeleteAPIView,
    tweet_action,
)

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list'),
    path('create/', TweetCreateAPIView.as_view(), name='create'),
    path('tweet-action/', tweet_action, name='tweet_action'),
    path('<pk>/', TweetDetailAPIView.as_view(), name='detail'),
    path('<pk>/update/', TweetUpdateAPIView.as_view(), name='update'),
    path('<pk>/delete/', TweetDeleteAPIView.as_view(), name='delete'),
]
