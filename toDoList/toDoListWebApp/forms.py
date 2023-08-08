from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<Your password can\'t be too similar to your other personal information. \nYour password must contain at least 8 characters. \nYour password can\'t be a commonly used password. \nYour password can\'t be entirely numeric.'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'



class TaskFrom(forms.ModelForm):
    taskDescription = forms.CharField(required=True, widget=forms.widgets.Textarea(
                                attrs={
                                    "placeholder": "What task must you perform?",
                                    "class": "form-control",
                                      }
                            ))
    class Meta:
        model = Tasks
        exclude = ("userId",)