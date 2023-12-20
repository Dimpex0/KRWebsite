from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Album, Image, Worker

from .forms import AlbumForm

from PIL import Image as PILImage
from io import BytesIO


def compress_image(image, quality=70):
    img = PILImage.open(image)

    compressed_image = BytesIO()
    img.save(compressed_image, format='JPEG', quality=quality)
    compressed_image.seek(0)
    return compressed_image


def home_page_view(request):
    if request.method == 'POST':
        if 'contact-form' in request.POST:
            try:
                form_data = request.POST
                first_name = form_data['first_name']
                last_name = form_data['last_name']
                email = form_data['email']
                phone = form_data['phone']
                message = form_data['message']
                html_message = render_to_string('mails/contact.html', {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone': phone,
                    'message': message,
                })
                plain_message = strip_tags(html_message)
                send_mail(
                    subject=f'KR Photography contact from {first_name}',
                    message=plain_message,
                    html_message=html_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[worker.email for worker in Worker.objects.all() or None]
                )
                messages.success(request, 'Message has been sent')
            except:
                messages.error(request, "Couldn't send message. Please try again later.")
            finally:
                return redirect('home page')
        if 'album-form' in request.POST:
            form = AlbumForm(request.POST, request.FILES)
            if form.is_valid():
                album_name = form.cleaned_data['name']
                cover_image = form.cleaned_data['cover_image']

                compressed_image = compress_image(cover_image, quality=70)

                album = Album()
                album.cover_image.save(cover_image.name, compressed_image, save=False)
                album.name = album_name
                album.save()
                messages.success(request, 'Successfully uploaded!')
                return redirect('home page')
            messages.error(request, "Couldn't upload album")
            return redirect('home page')
    context = {
        'albums': Album.objects.order_by('-id')[:3],
        'album_form': AlbumForm,
    }
    return render(request, 'home.html', context=context)


def album_page(request, pk, name):
    if request.method == 'POST':
        for file in request.FILES.getlist('files'):
            compressed_image = compress_image(file, quality=50)

            image = Image()
            image.image.save(file.name, compressed_image, save=False)
            image.album = Album.objects.get(pk=pk)
            image.save()
        messages.success(request, f'Successfully uploaded!')
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
