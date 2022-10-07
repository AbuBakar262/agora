from django.db import models
from django.utils.translation import gettext_lazy as _

class Advocate(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    short_bio = models.CharField(_('short bio'), max_length=100, blank=True, null=True)
    long_bio = models.TextField(_('long bio'), blank=True, null=True)
    advocate_years_exp = models.IntegerField(_('advocate years of experience'), blank=True, null=True)
    youtube = models.CharField(_('youtube link'), max_length=30, blank=True, null=True)
    twitter = models.CharField(_('twitter link'), max_length=30, blank=True, null=True)
    github = models.CharField(_('github link'), max_length=30, blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='advocate_user')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True, null=True)
    logo = models.ImageField(upload_to='profile/', null=True, blank=True)
    summary = models.TextField(_('summary'), blank=True, null=True)

    def __str__(self):
        return self.name