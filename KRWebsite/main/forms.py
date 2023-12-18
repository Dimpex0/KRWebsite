from django.forms import ModelForm
from .models import Album, Image


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
