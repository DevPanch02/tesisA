from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.users.models import User
from api.User.serializer_user import UserSerializer,UserTokenSerializerJWT,CustomUserSerializer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset
    
    def list(self,request):
        user = self.get_queryset()
        if user:
            user_serializer = self.serializer_class(user,many=True)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response({"message":"No hay ninguna usuario"}, status = status.HTTP_400_BAD_REQUEST)
    
    def create(self,request):
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            id_cli = User.objects.get(id = users_serializer.data['id'])
            self.send_email(id_cli.id)
            return Response({'message':'Usuario creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response( users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_email(self, id):
        user = User.objects.get(pk=id)
        to=user.email
        fromemail='muisne2022@outlook.es'
        subject='Términos y Condiciones'
        message = MIMEMultipart('alternative')
        message['subject'] = subject
        parameters = {
                'user': user,
                    #'mainpage': Mainpage.objects.first(),
                # 'link_home': 'http://{}'.format(url),
                    #'link_login': 'http://{}/login'.format(url),
        }
        html = render_to_string('correo.html', parameters)
        content = MIMEText(html, 'html')
        message.attach(content)

        mailserver = smtplib.SMTP('smtp.office365.com',587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()  #again
        mailserver.login('muisne2022@outlook.es', 'Muisne.2022')
        mailserver.sendmail(fromemail, to, message.as_string())
        mailserver.quit()
    


class Login(TokenObtainPairView):
    serializer_class = UserTokenSerializerJWT

    def post(self, request , *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            if user.is_active:
                print('EMAIL',user.email)
                print('id',user.id)
                login_serializer = self.serializer_class(data=request.data)
                if login_serializer.is_valid():
                    user_serializer = CustomUserSerializer(user)
                    arrayUser = [user_serializer.data]

                    # get_client_id = Client.objects.filter(user=user.id)
                    # for cli in get_client_id:
                    #     client_id = cli.id

                    return Response({
                        'token': login_serializer.validated_data.get('access'),
                        'refresh_token': login_serializer.validated_data.get('refresh'),
                        'user': arrayUser,
                        'message': 'Inicio de sesión Exitoso'
                    }, status= status.HTTP_200_OK)

                return Response({'message': 'Contraseña o nombre de usuario incorrecto'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Cuenta desabilitada'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'Contraseña o nombre de usuario incorrecto'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request , *args, **kwargs):
        # recibimos el id
        user = User.objects.filter(id=request.data.get('user',0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente'},status= status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario'}, status=status.HTTP_400_BAD_REQUEST)