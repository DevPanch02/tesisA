
from decimal import Decimal
from django.db import models
from core.users.models import User



class Person(models.Model):
    anio_tit=models.IntegerField(default=0, null=True, blank=True)
    num_reg=models.IntegerField(default=0, null=True, blank=True)
    RUC=models.CharField(max_length=15,default='', null=True, blank=True)
    nombrecomercial=models.CharField(max_length=500,default='', null=True, blank=True)
    razonsocial=models.CharField(max_length=100,default='', null=True, blank=True)
    calleprincipal=models.CharField(max_length=50,default='', null=True, blank=True)
    numerocasa=models.CharField(max_length=50,default='', null=True, blank=True)
    callesecundaria=models.CharField(max_length=50,default='', null=True, blank=True)
    sector=models.CharField(max_length=50,default='', null=True, blank=True)
    patrimonio=models.CharField(max_length=100, default='', null=True, blank=True)
    ced_ruc_representante=models.CharField(max_length=13,default='', null=True, blank=True)
    nombrerepresentante=models.CharField(max_length=200,default='', null=True, blank=True)
    apellidorepresentante=models.CharField(max_length=200,default='', null=True, blank=True)
    negociotipo=models.CharField(max_length=200,default='', null=True, blank=True)
    describenegocio=models.CharField(max_length=2000,default='', null=True, blank=True)
    rubro_pagado=models.CharField(max_length=50,default='', null=True, blank=True)
    valorpagar=models.FloatField(null=True, blank=True)
    fechpago=models.CharField(max_length=50,default='', null=True, blank=True)
    estadotitulo=models.CharField(max_length=10,default='', null=True, blank=True)
    fecharuc=models.CharField(max_length=50,default='', null=True, blank=True)
    fecharegmunicipio=models.CharField(max_length=50,default='', null=True, blank=True)
    abiertocerrado=models.CharField(max_length=10,default='', null=True, blank=True)
    fechacierre=models.CharField(max_length=50,default='', null=True, blank=True)
    canton_ruc=models.CharField(max_length=20,default='', null=True, blank=True)
    provincia_ruc=models.CharField(max_length=50,default=False)
    x=models.CharField(max_length=30,default='', null=True, blank=True)
    y=models.CharField(max_length=30,default='', null=True, blank=True)
    latitud=models.CharField(max_length=30,default='', null=True, blank=True)
    longitud=models.CharField(max_length=30,default='', null=True, blank=True)


    descripcion=models.TextField()


  




