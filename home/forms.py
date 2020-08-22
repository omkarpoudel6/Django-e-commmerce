from django import forms

class ContactForm(forms.Form):
    first_name=forms.CharField(max_length=30,
                               required=True,
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'}))
    last_name=forms.CharField(max_length=30,
                              required=True,
                              widget=forms.TextInput(attrs={'class':'form-control','placeholder':'LastName'}))
    email=forms.CharField(max_length=150,
                          required=True,
                          widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    subject=forms.CharField(max_length=255,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'subject'}))
    message=forms.CharField(max_length=1000,
                            required=True,
                            widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}))
