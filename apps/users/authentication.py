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
    
    expired =  False
    
    def expire_in(self, token):
        # Tiempo de expiraion
        
        time_elapsed = timezone.now() - token.created
        lef_time = timedelta(seconds= settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return lef_time

    def is_token_expired(self, token ):
        # Verifica si el toke expiro
        
        return self.expire_in(token) < timedelta(seconds = 0)

    def token_expire_hanndle(self, token):
        # Devuelve el valor de las anterior funciones
        
        is_expired = self.is_token_expired(token)         
        # Verificamos si el token expiro
        if is_expired:
            self.expired = True
            user = token.user
            token.delete()
            token =  self.get_model().objects.create(user = user)
        
        return is_expired, token
    
    def authenticate_credentials(self, key):
        # Se le agrega un tiempo de expiracion al token                
        
        message, token, user = None, None, None
        try:
            token =self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Invalido'
            self.expired = True
        
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado'
        
        if token is not None:
            is_expired = self.token_expire_hanndle(token)        
            if is_expired:
                message = 'Su token a expirado'

        return(token, user, message, self.expired)

