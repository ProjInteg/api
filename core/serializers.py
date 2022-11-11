from rest_framework import serializers
from .models import Cliente
from .models import Curso

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco', 'idade', 'email', 'curso')
        
