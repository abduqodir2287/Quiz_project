from django import forms
from .models import Users, Quiz

class Users_Forms(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class Quiz_forms(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"


