from django import forms
from .models import student

class stuform(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"