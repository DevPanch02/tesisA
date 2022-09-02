from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics

from core.startpage.models import Person
from .serializers import PersonSerializer, PersonUpdateSerializer

class PersonViewSet(viewsets.GenericViewSet):
    model = Person
    serializer_class = PersonSerializer
# 
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all().filter(valorpagar__gte=50.0).filter(descripcion='')
        return self.queryset
    
    def list(self,request):
        cart = self.get_queryset()
        if cart:
            cart_serializer = self.serializer_class(cart, many=True)
            return Response(cart_serializer.data, status = status.HTTP_200_OK)
        return Response({"message":"No hay ninguna pedido"}, status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        person_data = self.model.objects.filter(id=pk).first()
        if person_data:
            person_data_serializer = PersonUpdateSerializer(person_data,data=request.data)
            if person_data_serializer.is_valid():
                person_data_serializer.save()
                return Response({'message':'Datos de factura actualizado correctamente'}, status = status.HTTP_200_OK)
            return Response(person_data_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'message':'No se encontro esta factura'}, status = status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        billing_data = self.model.objects.filter(id=pk)
        if billing_data:
            billing_data_serializer = self.serializer_class(billing_data, many=True)
            return Response(billing_data_serializer.data, status = status.HTTP_200_OK)
        return Response({'message':'No se a encontrado ninguna dirección'}, status=status.HTTP_400_BAD_REQUEST)



#   LISTADO DE PERSONAS ADJUDICADAS
# class PersonViewSetAdjudicacion(viewsets.GenericViewSet):
#     model = Person
#     serializer_class = PersonSerializer
# # 
#     def get_queryset(self):
#         if self.queryset is None:
#             self.queryset = Person.objects.filter(rubro_pagado='ADJUDICACION DE ENTE PUBLICO A PERSONA NATURAL')
#         return self.queryset
    
#     def list(self,request):
#         cart = self.get_queryset()
#         if cart:
#             cart_serializer = self.serializer_class(cart, many=True)
#             return Response(cart_serializer.data, status = status.HTTP_200_OK)
#         return Response({"message":"No hay ninguna pedido"}, status = status.HTTP_400_BAD_REQUEST)
