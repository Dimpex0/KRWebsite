from django.urls import path

from .views import home_page_view, album_page, portfolio_view, update_album_view

urlpatterns = [
    path('', home_page_view, name='home page'),
    path('album/<pk>/<name>/', album_page, name='album page'),
    path('portfolio/', portfolio_view, name='portfolio page'),
    path('update-album/<int:pk>/', update_album_view, name='update album page'),
]

from .signals import *
