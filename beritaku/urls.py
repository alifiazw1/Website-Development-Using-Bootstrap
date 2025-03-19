from django.urls import path, include
from beritaku import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    # path('dashboard', views.dashboard, name='dashboard'),
    path('AboutUs', views.AboutUs, name='AboutUs'),
    path('Product', views.Product, name='Product'),
    path('Wardah', views.Wardah, name='Wardah'),
    path('SeaMakeup', views.SeaMakeup, name='SeaMakeup'),
    path('Implora', views.Implora, name='Implora'),
    path('Maybelline', views.Maybelline, name='Maybelline'),
    path('Makeover', views.Makeover, name='Makeover'),
    path('Shop', views.Shop, name='Shop'),
    path('Login', views.Login, name='Login'),
    path('pengguna', views.pengguna, name='pengguna'),
    path('keloladata', views.keloladata, name='keloladata'),
    path('lihatdata', views.lihatdata, name='lihatdata'),
    path('Admin', views.Admin, name='Admin'),
    path('Registrasi', views.Registrasi, name='Registrasi'),
    path('hapusdata/<int:berita_id>', views.hapusdata, name='hapusdata'),
    path('editdata/<int:berita_id>', views.editdata, name='editdata'),
    path('logout', views.Login, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# Create your views here.
