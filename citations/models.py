from django.db import models
from django.utils.translation import gettext as _

from wagtail.admin.edit_handlers import FieldPanel

from . import choices


class Citation(models.Model):
    citation_code = models.CharField("Citation code", max_length=32, primary_key=True)
    title = models.CharField("Title", max_length=512, null=True, blank=True)
    volume = models.CharField("Volume", max_length=255, null=True, blank=True)
    year = models.SmallIntegerField("Year", null=True, blank=True)
    issn = models.CharField("ISSN", max_length=9, null=True, blank=True)
    issn_size_set = models.SmallIntegerField("ISSN size set", null=True, blank=True)
    standardization_method = models.CharField("Standardization method", max_length=3, null=True, blank=True, choices=choices.STANDARDIZATION_METHOD)
    standardization_key = models.CharField("Standardization key", max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('citation_code'),
        FieldPanel('title'),
        FieldPanel('volume'),
        FieldPanel('year'),
        FieldPanel('issn'),
        FieldPanel('issn_size_set'),
        FieldPanel('standardization_method'),
        FieldPanel('standardization_key'),
    ]
