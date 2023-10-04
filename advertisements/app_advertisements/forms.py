from django import forms


class AdvertisementForms(forms.Form):
    title=forms.CharField(max_length=64, widget=forms.TextInput)
    description=forms.CharField(widget=forms.Textarea)
    price=forms.DecimalField(widget=forms.NumberInput)
    auction=forms.BooleanField(required=False, widget=forms.CheckboxInput)
    image=forms.ImageField(widget=forms.FileInput)