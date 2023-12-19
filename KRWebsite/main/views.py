from django.shortcuts import render, redirect

from .models import Album, Image

from .forms import AlbumForm

from PIL import Image as PILImage
from io import BytesIO


# TODO get compression to a function and add response messages

def home_page_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            album_name = form.cleaned_data['name']
            cover_image = form.cleaned_data['cover_image']
            img = PILImage.open(cover_image)

            compressed_image = BytesIO()
            img.save(compressed_image, format='JPEG', quality=50)
            compressed_image.seek(0)

            album = Album()
            album.cover_image.save(cover_image.name, compressed_image, save=False)
            album.name = album_name
            album.save()
            return redirect('home page')
    context = {
        'albums': Album.objects.order_by('-id')[:3],
        'album_form': AlbumForm,
    }
    return render(request, 'home.html', context=context)


def album_page(request, pk, name):
    if request.method == 'POST':
        print(request.FILES.getlist('files'))
        for file in request.FILES.getlist('files'):
            print(file)
            img = PILImage.open(file)

            compressed_image = BytesIO()
            img.save(compressed_image, format='JPEG', quality=50)
            compressed_image.seek(0)

            image = Image()
            image.image.save(file.name, compressed_image, save=False)
            image.album = Album.objects.get(pk=pk)
            image.save()
        if 'delete-image' in request.POST:
            image = Image.objects.get(pk=request.POST['delete-image'])
            image.delete()
        return redirect('album page', pk=pk, name=name)

    context = {
        'name': name,
        'pk': pk,
        'images': Image.objects.filter(album=pk)
    }
    return render(request, template_name='album.html', context=context)


def portfolio_view(request):
    if request.method == 'POST':
        if 'delete-album' in request.POST:
            album = Album.objects.get(pk=request.POST['delete-album'])
            album.delete()

        return redirect('portfolio page')
    context = {
        'albums': Album.objects.order_by('-id')
    }
    return render(request, 'portfolio.html', context=context)
