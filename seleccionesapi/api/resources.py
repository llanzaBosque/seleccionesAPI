from django.db.models import Q
from rest_framework import viewsets

from .serializers import SeleccionSerializer, PartidoSeliarizer, TipoPartidoSerializer
from ..models import Seleccion, Partido, Tipo_Partido


#Define las views para las selecciones
class SeleccionViewSet(viewsets.ModelViewSet):
    queryset = Seleccion.objects.all()
    serializer_class = SeleccionSerializer

    """
    Método que permite crear las selecciones, 
    y obtiene su probabilidad de ganar el mundial 
    según los resultados obtenidos en los partidos. 
    """

    # def perform_create(self, serializer):
    #     serializer.save(probabilidad=0)


    def definir_probabilidad(self):
        """
        TODO: Método para definir la probabilidad de que la selección gane el mundial.
        """
        # Se suma el puntaje obtenido en cada partido, estos puntajes se obtienen así:
        # P = M * I * T * C
        # M = Si: Ganó = 3, Empató = 1, Perdió = 0, Ganó por penales = 2, Perdió por penales = 1
        # I = si: Amistoso = 1, Mundial / Eliminatorias primera instancia = 2.5,
        # Eliminatorias última fase y copa confederaciones = 3, Mundial (después de octavos de final) = 4
        # T = Si es el primero en el ranking = 200, si está por debajo del 150 = 50,
        # en resto = 200 - posición en el ranking.
        # C = Si CONMEBOL = 1, UEFA = 0.99, AFC = 0.85, CAF = 0.85, OFC = 0.85, CONCACAF = 0.85
        # ***Cada vez que se incluya un partido se re calcula la probabilidad de las selecciones que participan

        return 100



#Define las views para los Partidos

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSeliarizer




#Define las views para los tipos de partido
class TipoPartidoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Partido.objects.all()
    serializer_class = TipoPartidoSerializer
