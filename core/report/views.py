from cgitb import html
from io import BytesIO
from django.template.loader import get_template
from django.shortcuts import render

#LIBRERIA
from xhtml2pdf import pisa
from core.startpage.models import Person
from django.views.generic import View
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render



#LIBRERIA
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result) 

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def vista(request):
    persona= Person.objects.all()


    data={
    'person':Person.objects.all().exclude(descripcion='').filter(valorpagar__gte=50.0),
    'count':persona.count(),
    'title':"REPORTE DE USUARIOS"
    }
    pdf=render_to_pdf('report.html',data)


    return HttpResponse(pdf, content_type='aplication/pdf')


def ver_datos(request):
    data={
        'title':'REPORTE DE NOTIFICADOR',
        'person':Person.objects.all().exclude(descripcion=''),
    }
    return render(request,'reportList.html',data)
# class Generar_reporte(View):
#     def get(self, request, *args, **kwargs):
#         template_name='report.html'
#         persona= Person.objects.all()
#         data={
#             'count':persona.count(),
#             'persona':persona
#         }
#         pdf=render_to_pdf(template_name,data)
#         return HttpResponse(pdf, content_type='aplication/pdf')

    


    

