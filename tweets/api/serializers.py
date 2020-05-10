from rest_framework import serializers
from tweets.models import Tweet


ACTIONS_TWEET_LIST = ['like', 'unlike', 'retweet'] 

class TweetAction(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()  
    content = serializers.CharField(allow_blank=True, required=False)  

    def validate_action(self, value):
        action_val = value.lower().strip()

        if action_val not in ACTIONS_TWEET_LIST:
            serializers.ValidationError('Action is not valid.')
        return value

class TweetParentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ['id', 'parent', 'user', 'content', 'image', 'likes', 'timestamp']

    def get_likes(self, obj):
        return obj.likes.count()


class TweetSerializer(serializers.ModelSerializer):
    parent = TweetParentSerializer(read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ['id', 'parent', 'user', 'content', 'image', 'likes', 'timestamp']

    def get_likes(self, obj):
        return obj.likes.count()
