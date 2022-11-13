from django.contrib import admin
from .models import Cliente
from core.models import Curso

admin.site.register(Cliente)
admin.site.register(Curso)

