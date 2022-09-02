from django.urls import path, include
from .views import vista,ver_datos
urlpatterns = [
    # path('users-report/', ReportView.as_view(), name='report'),
    path('ver-report/', ver_datos, name='ver_datos'),
    path('users-reportPDF/', vista, name='report_pdf'),

]
