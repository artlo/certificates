from django.http import QueryDict
from django.shortcuts import render_to_response, redirect, reverse
from django.template import RequestContext

from certificates.core.form import CertificateForm
from certificates.core.parse_certificate import parse_certificate, write_certificate_to_db


def overview(request):
    form = CertificateForm(request.GET)
    obj = None
    if form.is_valid():
        obj = form.cleaned_data['certificate']
    return render_to_response('overview.html', dict(certificate=obj))


def upload_certificate(request):
    if 'import_file' not in request.FILES:
        return redirect('overview')

    file_ = request.FILES['import_file']
    certificate = parse_certificate(file_)
    file_.close()
    cert_obj = write_certificate_to_db(certificate)
    param = QueryDict(mutable=True)
    param.update(dict(certificate=cert_obj.pk if cert_obj else ''))
    url = reverse('overview') + '?' + param.urlencode()
    return redirect(reverse('overview') + '?' + param.urlencode())
