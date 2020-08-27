from django import forms
from home.models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','subject','message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name and Surname'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','rows':'5'})
        }


class SearchForm(forms.Form):
    query=forms.CharField(max_length=100,required=True)
    catid=forms.IntegerField()