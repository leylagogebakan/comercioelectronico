# Python
from datetime import datetime
# Django
from django.contrib.sessions.models import Session
# Res Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# Apps : User
from apps.users.api.serializers import UserTokenSerialzier


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

