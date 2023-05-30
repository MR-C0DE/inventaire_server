from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the InventaireSerializer from the serializer file
from .serializers import InventaireSerializer

# import the Inventaire model from the models file
from .models import Inventaire

# create a class for the Inventaire model viewsets


class InventaireView(viewsets.ModelViewSet):

    # create a serializer class and
    # assign it to the InventaireSerializer class
    serializer_class = InventaireSerializer

    # define a variable and populate it
    # with the Inventaire list objects
    queryset = Inventaire.objects.all()
