from django.db import models


class Certificates(models.Model):
    country = models.CharField(max_length=128)
    organization = models.TextField()
    common_name = models.TextField()
    email = models.TextField()
    surname = models.TextField()

    def __str__(self):
        return u'{}: {}: {}'.format(self.country, self.organization, self.email)
