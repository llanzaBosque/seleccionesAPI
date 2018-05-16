from rest_framework import serializers

from seleccionesapi.models import Seleccion, Partido, Tipo_Partido, Cuartos, Final, GrupoA, GrupoB, GrupoC, GrupoD, GrupoE, GrupoF, GrupoG, GrupoH, Octavos, Podio, Semifinales, Tercerlugar

# Serializadores para los modelos

class SeleccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seleccion
        fields = ("__all__")
        #read_only_fields = ('probabilidad',)

class PartidoSeliarizer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = ("__all__")

class TipoPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Partido
        fields = ("__all__")

class CuartosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuartos
        fields = ("__all__")

class FinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Final
        fields = ("__all__")

class GrupoASerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoA
        fields = ("__all__")

class GrupoBSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoB
        fields = ("__all__")

class GrupoCSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoC
        fields = ("__all__")

class GrupoDSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoD
        fields = ("__all__")

class GrupoESerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoE
        fields = ("__all__")

class GrupoFSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoF
        fields = ("__all__")

class GrupoGSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoG
        fields = ("__all__")

class GrupoHSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoH
        fields = ("__all__")


class OctavosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Octavos
        fields = ("__all__")

class PodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podio
        fields = ("__all__")

class SemifinalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semifinales
        fields = ("__all__")

class TercerLugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tercerlugar
        fields = ("__all__")