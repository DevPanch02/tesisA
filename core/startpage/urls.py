from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('import/', import_files, name='import'),
    

    path('list_persons/', TemplateListPersons.as_view(), name='list_persons'),

    path('deudores/',deudores, name='deudores'),
    path('no-deudores/',noDeudoras, name='no_deudores'),
    path('total_usuarios/',total_usuarios, name='total_usuarios'),
    path('eliminar/',eliminar, name='eliminar_usuarios'),

    

]
