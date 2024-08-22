from .models import User,Post,PostImage,Comment,Like,Story
from django import forms


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = 'username','password'
#         widgets = {
#             'username':forms.TextInput(attrs={'class':'inp-fields' , 'placeholder':'Username'}),
#             'password':forms.PasswordInput(attrs={'class':'inp-fields','placeholder':'Password'})
#         }
#         labels = {
#             'username': '',
#             'password': '',
#         }
#         help_texts = {
#             'username': None,  # This removes the help text for the username field
#         }

# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'inp-fields',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'inp-fields',
            'placeholder': 'Password'
        })
        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['username'].help_text = None



class SignupForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'inp-fields', 'placeholder': 'Name'}),
        label=''
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'inp-fields', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'inp-fields', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'inp-fields', 'placeholder': 'Password'}),
        }
        labels = {
            'email': '',
            'username': '',
            'password': '',
        }

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        name = self.cleaned_data.get('name')
        first_name, last_name = name.split(' ', 1) if ' ' in name else (name, '')
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
