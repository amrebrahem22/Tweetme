from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    CreateAPIView, 
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from tweets.models import Tweet
from .serializers import TweetSerializer, TweetAction


class TweetListAPIView(ListAPIView):
    permission_classes = []
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


class TweetDetailAPIView(RetrieveAPIView):
    permission_classes = []
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


class TweetCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


class TweetUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


class TweetDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tweet.objects.all()


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def tweet_action(request, *args, **kwargs):
    serializer = TweetAction(data=request.data)
    if serializer.is_valid():
        tweet_id = serializer.data.get('id')
        action = serializer.data.get('action')
        content = serializer.data.get('content')

        tweet_obj = Tweet.objects.filter(id=tweet_id)
        if not tweet_obj.exists():
            return Response({}, 404)
        obj = tweet_obj.first()

        if action == 'like':
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        
        elif action == 'unlike':
            obj.likes.remove(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)

        elif action == 'retweet':
            new_tweet = Tweet.objects.create(user=request.user, content=content, parent=obj)
            serializer = TweetSerializer(new_tweet)
            return Response(serializer.data, status=200)
    
    return Response({}, status=200)
    



