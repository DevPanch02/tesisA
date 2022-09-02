from core.startpage.models import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('id','RUC','nombrecomercial','ced_ruc_representante','nombrerepresentante','apellidorepresentante',
        'negociotipo','describenegocio','rubro_pagado','valorpagar','canton_ruc','provincia_ruc','latitud','longitud','descripcion')

class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('descripcion',)