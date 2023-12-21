from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps import views as sitemap_views
from KRWebsite.main.sitemap import AlbumSitemap, PortfolioSitemap, HomeSitemap

from django.views.generic.base import TemplateView

sitemaps = {
    'Home': HomeSitemap,
    'Portfolio': PortfolioSitemap,
    'albums': AlbumSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KRWebsite.main.urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
