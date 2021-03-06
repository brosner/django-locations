# Creating a HiddenBaseForm. from djangosnippets.org.
# Author : Yashh (www.yashh.com)

from django import forms
from django.forms.forms import BoundField
from django.utils.translation import ugettext as _

class HiddenBaseForm(forms.BaseForm):
    def as_hidden(self):
        output = []
        for name, field in self.fields.items():
            bf = BoundField(self, field, name)
            output.append(bf.as_hidden())
        return u'\n'.join(output)

class LocationForm(forms.Form):
    place = forms.CharField(label=_("Place"))

class CheckinForm(HiddenBaseForm, forms.Form):
    place = forms.CharField(label=_("Place"))
    latitude = forms.FloatField(label=_("Latitude"))
    longitude = forms.FloatField(label=_("Longitude"))
