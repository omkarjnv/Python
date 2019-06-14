from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from students import models



class RegistartionForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2')

    def save(self,commit=True):
        user=super(RegistartionForm,self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user

class CreateStudent(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ('USN','name','sem','Dept')


class CreateTeacher(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['EID','name','Dept','Contact']

