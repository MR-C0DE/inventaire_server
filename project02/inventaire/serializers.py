# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Inventaire

# create a serializer class


class InventaireSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Inventaire
        fields = ('id', 'nom', 'description', 'sorte', 'quantite', 'seuil')
