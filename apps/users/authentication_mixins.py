# Rest Frameworck 
from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Apps : User
from apps.users.authentication import ExpiringTokenAuthetication

class Authentication(object):


    def get_user(self, request):
        # Verificamos que el user tenga su token y que sea correcto 
        
        token = get_authorization_header(request).split()
        if token:
            try:            
                token =  token[1].decode()
            except:
                return None 
            token_expire = ExpiringTokenAuthetication()

            user, token, message = token_expire.authenticate_credentials(token)
            if user != None and token != None:
                return user
            return message
        return None
    
    def dispatch(self, request, *arg, **kwargs):
        user = self.get_user(request)
        # Se encuentra token en la peticion
        if user is not None:
            if type(user) == str:
                response = Response(
                    {
                        'errors': user
                    }
                )
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type= 'application/json'
                response.renderer_context = {}
                return response
            return super().dispatch(request,*arg, **kwargs)
        response = Response (
            {
                'error': 'No se han enviado las redeciales.'
            }
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type= 'application/json'
        response.renderer_context = {}
        return response 
        