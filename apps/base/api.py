# Rest Frameworck
from rest_framework import generics


# Generamos una class generiaca que nos permite tomar el queryset del serializador
class GenericListAPIView(generics.ListAPIView):
    
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)