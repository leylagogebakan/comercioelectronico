# Rest Framewock
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Apps : User
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer


""" Utilizacion de decorador Method GET - POST  """
@api_view(['GET','POST'])
def user_api_view(request):
    
    # list
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserListSerializer(users, many = True)
        return Response(
            users_serializer.data,
            status= status.HTTP_200_OK
        )
   
   # create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
         
        # validate
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
            {
                'menssage': 'User Create'
            }, 
            status= status.HTTP_200_OK 
        )
        return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


""" Utilizacion de decoradores MEtjod GET - PUT - DELETE """
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request, pk = None):
    # queryset
    user = User.objects.filter(id = pk).first()
    
    if user:

        # retive
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status= status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            
            # validate
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status= status.HTTP_200_OK)
            return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        #delte
        elif request.method == 'DELETE':
            user.delete()
            return Response (
            {
                'message': 'User delete'
            }, 
            status= status.HTTP_200_OK
        )
    return Response(
        {
            'message': 'User does not exist'
        },
        status= status.HTTP_400_BAD_REQUEST
    )


