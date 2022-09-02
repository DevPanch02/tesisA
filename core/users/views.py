from django.urls import reverse_lazy
import json
from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.startpage.models import Person

from core.users.forms import UserForm, UserEditForm
from core.users.models import User
from core.users.mixins import IsSuperuserMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


class listarUsuarios(IsSuperuserMixin, ListView):
    model = User
    template_name = 'list_user.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        person = User.objects.all().exclude(is_superuser=1)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Notificadores'
        context['create_url'] = reverse_lazy('users:user_create')
        context['list_url'] = reverse_lazy('users:user_list')
        context['user']=person

        return context


class UserCreateView(CreateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('users:user_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'dni':
                if User.objects.filter(dni=obj):
                    data['valid'] = False
            elif type == 'username':
                if User.objects.filter(username__icontains=obj):
                    data['valid'] = False
            elif type == 'email':
                if User.objects.filter(email=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Usuario'
        context['action'] = 'add'
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserEditForm
    success_url = reverse_lazy('users:user_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'username':
                if User.objects.filter(username__icontains=obj):
                    data['valid'] = False
            elif type == 'email':
                if User.objects.filter(email=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Usuario'
        context['action'] = 'add'
        return context


class DeleteView (DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:user_list')
    url_redirect = success_url


    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        return context


def cambiarPass(request):
    return render(request,'changePassword.html')