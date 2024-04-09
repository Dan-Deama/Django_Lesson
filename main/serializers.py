from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'telefone',
            'email',
            'data_nascimento',
            'description',
            'user',
        ]