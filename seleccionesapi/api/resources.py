from rest_framework import viewsets

from .serializers import SeleccionSerializer, PartidoSeliarizer
from ..models import Seleccion, Partido


#Define las views para las selecciones
class SeleccionViewSet(viewsets.ModelViewSet):
    queryset = Seleccion.objects.all()
    serializer_class = SeleccionSerializer

    """
    Método que permite crear las selecciones, 
    y obtiene su probabilidad de ganar el mundial 
    según los resultados obtenidos en los partidos. 
    """

    def perform_create(self, serializer):
        serializer.save(probabilidad=self.definir_probabilidad(), goles = self.definir_goles())


    def definir_probabilidad(self):
        """
        TODO: Método para definir la probabilidad de que la selección
        gane el mundial.
        """
        return 100

    def definir_goles(self):
        """
        TODO: Método para definir los goles de la selección
        gane el mundial.
        """
        return 100

#Define las views para los Partidos
class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSeliarizer

