from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Song(AbstractUser):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    album_thumbnail = models.ImageField(upload_to='album_thumbnails/', null=True, blank=True)
    audio_file = models.FileField(upload_to='songs/', null=True, blank=True)
    download_count = models.IntegerField(default=0)

    # Related name qo'shish
    groups = models.ManyToManyField(
        Group,
        related_name='song_user_set',  # Bu joyni o'zgartiring
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='song_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='song_user_permissions',  # Bu joyni o'zgartiring
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='song_user_permission'
    )

    def __str__(self):
        return self.song_name
