from django import forms


class SendEmailForm(forms.Form):
    name = forms.CharField(max_length=50)
    to = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(required=True, widget=forms.Textarea)
