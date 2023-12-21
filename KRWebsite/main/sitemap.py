from django.contrib.sitemaps import Sitemap
from .models import Album


class AlbumSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return Album.objects.all()


class HomeSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        # Return the objects you want to include in the sitemap (in this case, just the homepage)
        return ['home']

    def location(self, obj):
        # Define the URL for the 'home' page
        return '/'


class PortfolioSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        # Return the objects you want to include in the sitemap (in this case, just the homepage)
        return ['home']

    def location(self, obj):
        # Define the URL for the 'home' page
        return '/portfolio'
