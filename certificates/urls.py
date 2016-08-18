from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('', include('certificates.core.urls')),
    url(r'^admin/', admin.site.urls),
]
