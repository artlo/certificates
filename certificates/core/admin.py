from django.contrib import admin

from certificates.core.models import Certificates


class CertificatesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Certificates, CertificatesAdmin)