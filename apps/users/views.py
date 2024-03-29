# Python
from datetime import datetime
# Django
from django.contrib.sessions.models import Session
# Res Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# Apps : User
from apps.users.api.serializers import UserTokenSerialzier

class UserToken(APIView):
    """
    De esta manera traemos el neuvo token
    """
    def get (self, request, *arg, **kwargs):
        username = request.GET.get('username')
        try :
            user_token = Token.objects.get(
                user = UserTokenSerialzier().Meta.model.objects.filter(username = username).first()
            )
            return Response(
                {
                    'token': user_token.key
                },
                status = status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    'error': 'Credenciales enviadas incorrectas'
                },
                status = status.HTTP_400_BAD_REQUEST
                )


class Login(ObtainAuthToken):

    def post (self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data= request.data, context = {'request': request})  
        
        # Si es validoe s porque ya tiene usuario y contrase;a asociado
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:

                # Si tiene un token lo trae en el caso contrario se lo creea 
                token,create = Token.objects.get_or_create(user = user)
                user_serialzier = UserTokenSerialzier(user)
                if create:
                    return Response(
                        {
                            'token': token.key,
                            'user': user_serialzier.data,
                            'message': 'Inicio de sesion exitoso'
                        },
                        status= status.HTTP_201_CREATED
                    )
                else: 
                    """
                    # De esta manera no permitimos que haya mas de una cuenta abierrta al mismo timpo
                    all_session = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()

                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response(
                        {
                            'token': token.key,
                            'user': user_serialzier.data,
                            'message': 'Inicio de sesion exitoso'
                        },
                        status= status.HTTP_201_CREATED
                    )token.delete()
                    """
                    token.delete()
                    # El Usuario ya esta iniciado
                    return Response(
                        {
                        'error': 'Ya se inicio session con este usuario.'
                        }, status = status.HTTP_409_CONFLICT
                    )
            else:
                return Response(
                    {
                        'error': 'Este usuario no puede iniciar sesion'
                    },
                    status= status.HTTP_401_UNAUTHORIZED
                )
        else:
            return Response(
                {
                    'error': 'Nombre de usuario o contrase;a incorrecta'
                },
                status= status.HTTP_400_BAD_REQUEST
            )

class Logout(APIView):
    
    def post(self, request, *arg, **kwargs):
        try:

            # Recuperamos el token enviado
            token = request.POST.get('token')
            token =  Token.objects.filter(key = token).first()
            if token:
                user = token.user 
                all_session = Session.objects.filter(expire_date__gte = datetime.now())
                if all_session.exists():
                    for session in all_session:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado'
                return Response(
                    {
                        'token_message': token_message,
                        'session_message' : session_message
                    },
                    status= status.HTTP_200_OK
                )
            return Response(
                { 
                    'error': 'No se encontro un usuario con estas credenciales'
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {
                    'error': 'No se a encontrado token en la peticion'
                },
                status= status.HTTP_409_CONFLICT
            )

