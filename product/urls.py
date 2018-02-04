from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from product.views import *

urlpatterns = [
    url(r'^$', index, name='product_home'),
    url(r'^search-product/', search_product, name='search-product')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
