from django.dispatch import receiver
from .models import Album, Image
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Album)
def album_delete_signal(instance, *args, **kwargs):
    instance.cover_image.delete()


@receiver(pre_delete, sender=Image)
def image_delete_signal(instance, *args, **kwargs):
    instance.image.delete()
