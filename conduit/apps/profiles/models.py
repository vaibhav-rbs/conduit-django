from django.db import models

from conduit.apps.core.models import TimestampedModel

class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE)
    
    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False )

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.follows.add(profile)
    
    def unfollow(self, profile):
        self.follow.remove(profile)
    
    def is_following(self, profile):
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        return self.followed_by.filter(pk=profile.pk).exists()
