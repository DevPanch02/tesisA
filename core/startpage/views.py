from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from requests import Response
from .resources import PersonResource
from tablib import Dataset
from django.db.models import Q

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.views.generic.base import TemplateView

from .models import *
from .forms import *
from core.users.models import User


# Create your views here.
class TemplateListPersons(TemplateView):
    template_name = "datatable/table.html"

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'
        return context


class Home(TemplateView):
    template_name = "index.html"

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        person = Person.objects.all()
        person_deudore = Person.objects.filter(valorpagar__gte=50.0)
        person_no_deudore = Person.objects.filter(valorpagar__lt=20.0)
        users1 = User.objects.filter(is_superuser=0)
        context = super().get_context_data(**kwargs)
        context["title"] = "Panel inicio"
        context["person"] = person.count()
        context["person_deudor"] = person_deudore.count()
        context["person_no_deudore"] = person_no_deudore.count()
        context["users"] = users1.count()
        return context

#   IMPORT FILE EXCEL (XLS)


def import_files(request):

    try:
        if request.method == 'POST':
            person_resource = PersonResource()
            dataset = Dataset()
            new_person = request.FILES['myfile']

            if not (new_person.name.endswith('xls') or new_person.name.endswith('xlsx')):
                messages.info(request, 'FORMATO INCORRECTO')
                return render(request, 'index.html')

            imported_data = dataset.load(new_person.read(), format='xls')
            for data in imported_data:
                """ value=Person(
                    data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],
                    data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],
                    data[16],data[17]
                ) """

                persona = Person()
                persona.anio_tit = data[0]
                persona.num_reg = int(data[1])
                persona.RUC = data[2]
                persona.nombrecomercial = data[3]
                persona.razonsocial = data[4]
                persona.calleprincipal = data[5]
                persona.numerocasa = data[6]
                persona.callesecundaria = data[7]
                persona.sector = data[8]
                persona.patrimonio = data[9]
                persona.ced_ruc_representante = data[10]
                persona.nombrerepresentante = data[11]
                persona.apellidorepresentante = data[12]
                persona.negociotipo = data[13]
                persona.describenegocio = data[14]
                persona.rubro_pagado = data[15]
                persona.valorpagar = data[16]
                persona.fechpago = data[17]
                persona.estadotitulo = data[18]
                persona.fecharuc = data[19]
                persona.fecharegmunicipio = data[20]
                persona.abiertocerrado = data[21]
                persona.fechacierre = data[22]
                persona.canton_ruc = data[23]
                persona.provincia_ruc = data[24]
                persona.x = data[25]
                persona.y = data[26]
                persona.latitud = data[27]
                persona.longitud = data[28]
                # if data[27] == '' or data[28] == '':
                #     print('exito')

                persona.save()

            messages.success(request, "Datos cargados")
    except:
        messages.warning(request,"NO AH CARGADO NINGUN ARCHIVO")
        return render(request, 'index.html')
    return render(request, 'files/import.html', {'title': 'Importacion de datos'})


#   IMPORTED TIP OF DATA

def deudores(request):
    deudores = {
        'title':'PERSONAS DEUDORAS',
        'persons': Person.objects.filter(valorpagar__gte=50.0),
    }

    return render(request, 'files/import.html', deudores)

def noDeudoras(request):
    deudores = {
        'title':'PERSONAS DEUDORAS',
        'persons': Person.objects.filter(valorpagar__lte=50.0),
    }
    return render(request, 'files/import.html', deudores)

def total_usuarios(request):
    total = {
        'persons': Person.objects.all(),
        'title': 'LISTADO USUARIOS',
        'date_now': ''
    }
    return render(request, 'datatable/table.html', total)

def eliminar(request):
    persons=Person.objects.all()
    persons.delete()
    messages.warning(request,"USUARIOS ELIMINADOS")
    return render(request, 'index.html')

class Error404(TemplateView):
    template_name='startpage/404.html'

class Error500(TemplateView):
    template_name='startpage/500.html'

    @classmethod
    def as_error_view(cls):
        v=cls.as_view()
        def view(request):
            r=v(request)
            r.render()
            return r
        return view
