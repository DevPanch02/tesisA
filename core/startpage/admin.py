from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display=('anio_tit','num_reg','RUC','nombrecomercial','razonsocial','calleprincipal','numerocasa',
    'callesecundaria','sector','patrimonio','ced_ruc_representante','nombrerepresentante','apellidorepresentante',
    'negociotipo','describenegocio','rubro_pagado','valorpagar','fechpago','estadotitulo','fecharuc','fecharegmunicipio',
    'abiertocerrado','fechacierre','canton_ruc','provincia_ruc','x', 'y','latitud','longitud')

# admin.site.register(User)