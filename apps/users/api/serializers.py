# Res
from rest_framework import serializers
# App
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User """
    class Meta:
        model = User
        fields = '__all__'

    # Encrriptado de contrase;a
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    """ Serializer for User. Method GET """
    class Meta:
        model = User

    # De esta manera podemos redefinir y indicar que queremos mostrar a la hora de listar
    def to_representation(self, instance):       
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password'], 
        }

