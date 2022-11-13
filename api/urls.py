from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet
from rest_framework import routers
from core.views import CursoViewSet


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'cursos', CursoViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
    ]   
