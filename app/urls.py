from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$',views.index,name='home'),
    url('^home/$',views.homepage,name='index'),
    url('^accounts/profile/upload/',views.upload_image,name='upload'),
    url('^accounts/profile/$',views.prof,name='prof'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)