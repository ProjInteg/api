from django.db import models
from random import choices


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    curso = models.CharField(max_length=50)
    
    
   
class Curso(models.Model):
        
        cursoChoices = (
            ('1', ' Desenho e Pintura'),
        
            ('2', 'Curso de cerâmica'),
        
            ('3', 'Retrato com modelo vivo'),
        
            ('4', 'paisagem/3ª idade'),
        
            ('5', 'Aquarela (aula quinzenal'),
        
            ('6', 'seção modelo vivo')
         )
        
        curso = models.CharField(max_length=50, default="Novo Curso", choices=cursoChoices)
        novoCursoNome = models.CharField(max_length=50, default="Novo Curso")
    
        def __str__(self):
            return self.curso
        
        
        

