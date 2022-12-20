from rest_framework import serializers
from .models import Becas
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class BecasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Becas
        fields = ['id', 'nombre', 'porcentaje', 'pais', 'universidad', 'requerimiento']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        #Ocultar la clave
     #   extra_kwargs = {'password': {
      #      'write_only': True,
      #      'required': True
      #  }}

    #Crear clave automaticamente
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user