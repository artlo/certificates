from django.conf.urls import url

from certificates.core.views import upload_certificate, overview

urlpatterns = [
    url(r'^$', overview, name='overview'),
    url(r'^upload_certificate/$', upload_certificate, name='upload-file'),
]
