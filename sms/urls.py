from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BASE,name='base'),




    # This is admin urls
    path('dashboard/addressbook/', views.ADDRESSBOOK,name='addressbook'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
