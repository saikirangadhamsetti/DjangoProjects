from django import forms
from todo.models import Todo
class todolist(forms.ModelForm):
    class meta:
        model=Todo
        fields="_all_"