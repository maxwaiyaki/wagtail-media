from __future__ import absolute_import, unicode_literals

from wagtailmedia.widgets import AdminMediaChooser

from wagtail.admin.edit_handlers import BaseChooserPanel


class BaseMediaChooserPanel(BaseChooserPanel):
    object_type_name = 'media'

    def widget_overrides(self):
        return {self.field_name: AdminMediaChooser}


class MediaChooserPanel(object):
    def __init__(self, field_name):
        self.field_name = field_name

    def bind_to_model(self, model):
        return type(str('_MediaChooserPanel'), (BaseMediaChooserPanel,), {
            'model': model,
            'field_name': self.field_name,
        })
