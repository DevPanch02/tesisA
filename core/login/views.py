from email import message
from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import RedirectView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class LoginFormView(LoginView):
    template_name='login.html'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return render(request,'index.html')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['title']="Iniciar Session"
        return context


class LogoutRedirectView(RedirectView):
    pattern_name='login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)