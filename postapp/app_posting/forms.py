from django import forms
from .models import Post,comment,Tags
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MycreationForm(UserCreationForm):
    Email=forms.EmailField()
    Fistname=forms.CharField()
    Lastname=forms.CharField()
    class Meta:
        model=User
        fields=['username','Email','Fistname','Lastname','password1','password2',]

class posting(forms.Form):
    title=forms.CharField(max_length=20)
    description=forms.CharField(max_length=2000)
    tags=forms.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"



class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields='__all__'



