from django import forms

class GuideForm(forms.Form):

    name = form.CharField(label='Title', max_length=200)
    description = form.TextField(label='Description',widget=forms.Textarea())
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
