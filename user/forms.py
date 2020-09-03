from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from user.models import UserProfile

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=30,label="User Name")
    email=forms.EmailField(max_length=100,label="Email")
    first_name=forms.CharField(max_length=30,label='First Name')
    last_name=forms.CharField(max_length=30,label='Last Name')

    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2',)

class UserUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name',)
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'})
        }

CITY=[
    ('Itahari','Itahari'),
    ('Dharan','Dharan'),
    ('Kathmandu','Kathmandu'),
    ('Pokhara','Pokhara')
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone','address','city','country','image',)
        widgets={
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'city':forms.Select(attrs={'class':'form-control','placholder':'city'},choices=CITY),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'image'})
        }
