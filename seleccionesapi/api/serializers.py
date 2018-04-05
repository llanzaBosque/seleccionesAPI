from rest_framework import serializers

from seleccionesapi.models import Seleccion, Partido, Tipo_Partido


class SeleccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seleccion
        fields = ("__all__")
        read_only_fields = ('probabilidad',)

class PartidoSeliarizer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ("__all__")

class TipoPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Partido
        fields = ("__all__")
