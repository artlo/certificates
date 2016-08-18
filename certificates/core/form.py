from django.forms import Form, ModelChoiceField

from certificates.core.models import Certificates


class CertificateForm(Form):
    certificate = ModelChoiceField(queryset=Certificates.objects.all(), required=False)
