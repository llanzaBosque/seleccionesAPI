from rest_framework import serializers

from seleccionesapi.models import Seleccion, Partido


class SeleccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seleccion
        fields = ("__all__")
        read_only_fields = ('probabilidad', 'goles')

class PartidoSeliarizer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ("__all__")
