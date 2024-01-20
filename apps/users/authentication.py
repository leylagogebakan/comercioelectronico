# Python
from datetime import timedelta
# Django
from django.utils import timezone
from django.conf import settings
# Res Framework
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed



class ExpiringTokenAuthetication (TokenAuthentication):
    """
    Class que nos permite ponerle un tiempoo de expiracion a el token
    """

    def expire_in(self, token):
        """
        Tiempo de expiraion
        """
        time_elapsed = timezone.now() - token.create
        lef_time = timedelta(seconds= settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return lef_time

    def is_token_expired(self, token ):
        """
        Verifica si el toke expiro
        """
        return self.expire_in(token) < timedelta(seconds = 0)

    def token_expire_hanndle(self, token):
        """
        Devuelve el valor de las anteriores funciones
        """
        is_expired = self.is_token_expired(token)        
        if is_expired:
            print('Token expirado')
        return is_expired
    
    def authenticate_credentials(self, key):
        """
        Se le agrega un tiempo de expiracion al token
        """        
        try:
            token =self.get_model().objects.select_related('user').get(key = key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Token Invalido')
        
        if not token.user.is_active:
            raise AuthenticationFailed('Usuario no activo o eliminado')
        
        is_expired = self.token_expire_hanndle(token)
        if is_expired:
            raise AuthenticationFailed('Su9 toklen a expirado')
        
        return(token.user.token)

