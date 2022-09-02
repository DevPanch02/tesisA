
from .models import *
from django import forms


from .models import *

class PersonRegistration(forms.ModelForm):
    class Meta:
        model = Person
        fields='__all__'
