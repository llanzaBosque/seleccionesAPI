from django.db.models import Q
from rest_framework import viewsets

from .serializers import SeleccionSerializer, PartidoSeliarizer, TipoPartidoSerializer, CuartosSerializer, FinalSerializer, GrupoASerializer, GrupoBSerializer, GrupoCSerializer, GrupoDSerializer, GrupoESerializer, GrupoFSerializer, GrupoGSerializer, GrupoHSerializer, OctavosSerializer, PodioSerializer, SemifinalesSerializer, TercerLugarSerializer
from ..models import Seleccion, Partido, Tipo_Partido, Cuartos, Final, GrupoA, GrupoB, GrupoC, GrupoD, GrupoE, GrupoF, GrupoG, GrupoH, Octavos, Podio, Semifinales, Tercerlugar


#Define las views para las selecciones
class SeleccionViewSet(viewsets.ModelViewSet):
    queryset = Seleccion.objects.all()
    serializer_class = SeleccionSerializer

#Define las views para los Partidos

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSeliarizer


#Define las views para los tipos de partido
class TipoPartidoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Partido.objects.all()
    serializer_class = TipoPartidoSerializer

#Define las views para los cuartos
class CuartosViewSet(viewsets.ModelViewSet):
    queryset = Cuartos.objects.all()
    serializer_class = CuartosSerializer

#Define las views para la final
class FinalViewSet(viewsets.ModelViewSet):
    queryset = Final.objects.all()
    serializer_class = FinalSerializer

#Define las views para los GrupoA
class GrupoAViewSet(viewsets.ModelViewSet):
    queryset = GrupoA.objects.all()
    serializer_class = GrupoASerializer

#Define las views para los GrupoB
class GrupoBViewSet(viewsets.ModelViewSet):
    queryset = GrupoB.objects.all()
    serializer_class = GrupoBSerializer

#Define las views para los GrupoC
class GrupoCViewSet(viewsets.ModelViewSet):
    queryset = GrupoC.objects.all()
    serializer_class = GrupoCSerializer

#Define las views para los GrupoD
class GrupoDViewSet(viewsets.ModelViewSet):
    queryset = GrupoD.objects.all()
    serializer_class = GrupoDSerializer

#Define las views para los GrupoE
class GrupoEViewSet(viewsets.ModelViewSet):
    queryset = GrupoE.objects.all()
    serializer_class = GrupoESerializer

#Define las views para los GrupoA
class GrupoFViewSet(viewsets.ModelViewSet):
    queryset = GrupoF.objects.all()
    serializer_class = GrupoFSerializer

#Define las views para los GrupoA
class GrupoGViewSet(viewsets.ModelViewSet):
    queryset = GrupoG.objects.all()
    serializer_class = GrupoGSerializer

#Define las views para los GrupoA
class GrupoHViewSet(viewsets.ModelViewSet):
    queryset = GrupoH.objects.all()
    serializer_class = GrupoHSerializer

#Define las views para los GrupoA
class OctavosViewSet(viewsets.ModelViewSet):
    queryset = Octavos.objects.all()
    serializer_class = OctavosSerializer

#Define las views para los GrupoA
class PodioViewSet(viewsets.ModelViewSet):
    queryset = Podio.objects.all()
    serializer_class = PodioSerializer

#Define las views para los GrupoA
class SemifinalesViewSet(viewsets.ModelViewSet):
    queryset = Semifinales.objects.all()
    serializer_class = SemifinalesSerializer

#Define las views para los GrupoA
class TercerLugarViewSet(viewsets.ModelViewSet):
    queryset = Tercerlugar.objects.all()
    serializer_class = TercerLugarSerializer
