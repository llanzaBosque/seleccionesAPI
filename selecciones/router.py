from rest_framework.routers import SimpleRouter

from seleccionesapi.api.resources import SeleccionViewSet, PartidoViewSet

from django.urls import include, path

#Define automáticamente las urls necesarias
router = SimpleRouter()
router.register('selecciones',viewset=SeleccionViewSet)
router.register('partidos', viewset=PartidoViewSet)

urlpatterns = [
    path('',include(router.urls))
]