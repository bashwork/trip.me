from django.forms import ModelForm
from guides.models import Guide

class GuideForm(ModelForm):
    class Meta:
        model = Guide
        exclude = ('created', 'modified', 'user')
