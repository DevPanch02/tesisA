from pyexpat import model
from crum import get_current_request
from django import forms
from django.contrib.auth import update_session_auth_hash
from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'password', 'dni', 'email', 'groups', 'image', 'is_active'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus nombres'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese sus apellidos'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese un username'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese su número de cedula'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Ingrese un password'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control-checkbox'})
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token','groups']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()


                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class UserEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'password', 'email', 'image', 'is_active'
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly':True,'title':'No sepuede modificar'}),
            'last_name': forms.TextInput(attrs={'readonly':True,'title':'No sepuede modificar'}),
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese un username'}),
            'dni': forms.TextInput(attrs={'readonly':True,'title':'No sepuede modificar'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
            'password': forms.PasswordInput(render_value=True, attrs={'readonly':True,'title':'No sepuede modificar'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control-checkbox'})
        }
        exclude = ['is_change_password', 'is_staff', 'user_permissions', 'date_joined',
                   'last_login', 'is_superuser', 'token','groups']

    def update_session(self, user):
        request = get_current_request()
        if user == request.user:
            update_session_auth_hash(request, user)

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()


                self.update_session(u)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

        ##  EDITAR
    