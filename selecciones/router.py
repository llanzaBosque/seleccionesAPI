from rest_framework.routers import SimpleRouter

from seleccionesapi.api.resources import SeleccionViewSet, PartidoViewSet, TipoPartidoViewSet, CuartosViewSet, FinalViewSet, GrupoAViewSet, GrupoBViewSet, GrupoCViewSet, GrupoDViewSet, GrupoEViewSet, GrupoFViewSet, GrupoGViewSet, GrupoHViewSet, OctavosViewSet, PodioViewSet, SemifinalesViewSet, TercerLugarViewSet
from django.urls import include, path

#Define automáticamente las urls necesarias
router = SimpleRouter()
router.register('selecciones',viewset=SeleccionViewSet)
router.register('partidos', viewset=PartidoViewSet)
router.register('tipos_partido', viewset=TipoPartidoViewSet)
router.register('cuartos', viewset=CuartosViewSet)
router.register('final', viewset=FinalViewSet)
router.register('grupoa', viewset=GrupoAViewSet)
router.register('grupob', viewset=GrupoBViewSet)
router.register('grupoc', viewset=GrupoCViewSet)
router.register('grupod', viewset=GrupoDViewSet)
router.register('grupoe', viewset=GrupoEViewSet)
router.register('grupof', viewset=GrupoFViewSet)
router.register('grupog', viewset=GrupoGViewSet)
router.register('grupoh', viewset=GrupoHViewSet)
router.register('octavos', viewset=OctavosViewSet)
router.register('podio', viewset=PodioViewSet)
router.register('semifinales', viewset=SemifinalesViewSet)
router.register('tercerlugar', viewset=TercerLugarViewSet)

urlpatterns = [
    path('',include(router.urls))
]