from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username','password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Password'}),
            'first_name': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Username'}),
            'email': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Email'}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Password'}),
            'username': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Username'}),
        }