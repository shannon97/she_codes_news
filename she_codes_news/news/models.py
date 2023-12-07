from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    story_image = models.URLField(blank=True, null=True)

    def delete_story(self, user):
        return user == self.author

class Comments(models.Model):
    post = models.ForeignKey(NewsStory, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        get_user_model(),
        related_name= 'comments',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author} said: {self.created_on}"
