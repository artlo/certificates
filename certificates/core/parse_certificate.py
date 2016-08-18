from OpenSSL import crypto

from certificates.core.models import Certificates

__all__ = ['parse_certificate', 'write_certificate_to_db']

PEM_EXT = 'pem'
COMPONENTS_MAPPING = {
    'C': 'country',
    'O': 'organization',
    'CN': 'common_name',
    'SN': 'surname',
    'emailAddress': 'email'
}

def get_certificate_type(file_):
    ext = file_.name.lower().split('.')[-1]
    if ext == PEM_EXT:
        return crypto.FILETYPE_PEM
    return crypto.FILETYPE_ASN1


def get_subject(file_):
    cert = crypto.load_certificate(get_certificate_type(file_), file_.read())
    return cert.get_subject().get_components()


def parse_components(components):
    result = {}
    for key, value in components:
        try:
            # it's possibly needs string decoding for value
            result[COMPONENTS_MAPPING[key]] = value
        except KeyError:
            continue
    return result


def parse_certificate(file_):
    try:
        subject_components = get_subject(file_)
    except Exception:
        subject_components = []

    return parse_components(subject_components)


def write_certificate_to_db(certificate):
    if not certificate:
        return
    cert = Certificates(**{k: v for k, v in certificate.iteritems()})
    cert.save()
    return cert
