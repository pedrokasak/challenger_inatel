from rest_framework import serializers
from ..models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Criação da API para a App Users

        pegando todos os parametros da models Users 

        """
        model = Users
        fields = '__all__'
