from django.utils.translation import gettext as _

from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import (Citation)


class CitationAdmin(ModelAdmin):
    model = Citation
    menu_label = 'Citations'
    menu_icon = 'folder'
    menu_order = 000
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        'citation_code',
        'title',
        'volume',
        'year',
        'issn',
        'standardization_method',
        'issn_size_set',
        'standardization_key',
    )
    list_filter = (
        'title',
        'year',
        'issn',
        'standardization_method',
        'issn_size_set',
    )
    search_fields = (
        'citation_code',
        'title',
        'volume',
        'year',
        'issn',
        'standardization_method',
        'issn_size_set',
    )


modeladmin_register(CitationAdmin)
