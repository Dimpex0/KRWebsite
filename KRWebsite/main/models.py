from django.db import models
from django.urls import reverse


class Album(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    cover_image = models.ImageField(
        upload_to='albums',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('album page', kwargs={'pk': self.pk, 'name': self.name})


class Image(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    image = models.ImageField(
        upload_to='images',
        null=False,
        blank=False,
    )


class Worker(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    email = models.EmailField(
        null=False,
        blank=False
    )
