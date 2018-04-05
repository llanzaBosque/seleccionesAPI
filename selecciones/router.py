from rest_framework.routers import SimpleRouter

from seleccionesapi.api.resources import SeleccionViewSet, PartidoViewSet, TipoPartidoViewSet

from django.urls import include, path

#Define automáticamente las urls necesarias
router = SimpleRouter()
router.register('selecciones',viewset=SeleccionViewSet)
router.register('partidos', viewset=PartidoViewSet)
router.register('tipos_partido', viewset=TipoPartidoViewSet)

urlpatterns = [
    path('',include(router.urls))
]