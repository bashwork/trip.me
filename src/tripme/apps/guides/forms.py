from django import forms

class GuideForm(forms.Form):
    class Meta:
        model = Guide
