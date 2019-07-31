from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$', views.index, name='home'),
    url('^home/$', views.homepage, name='index'),
    url('^accounts/profile/upload/', views.image_upload, name='upload'),
    url('^accounts/profile/$', views.profile, name='profile'),
    url('^accounts/profile/upload_image/$', views.upload_image, name='upload_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
