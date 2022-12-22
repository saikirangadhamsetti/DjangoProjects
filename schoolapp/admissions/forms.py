from django import forms
from admissions.models import student
class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"
class normalform(forms.Form):
    name=forms.CharField(max_length=10)
    contact=forms.IntegerField(max_value=50000000)
    address=forms.CharField(max_length=50)
class kk(forms.Form):
    id=forms.IntegerField()