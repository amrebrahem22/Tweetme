from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def upload_tweet_image_path(instance, filename):
    return 'tweets/{}_{}'.format(instance.content[:15], filename)

class TweetLike(models.Model):
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.tweet.content[:10], self.user.username)


class Tweet(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_tweet_image_path, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='user_like', through=TweetLike, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.content[:10], self.user.username)
