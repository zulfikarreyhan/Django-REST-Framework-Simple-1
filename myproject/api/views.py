from itsdangerous import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    Serializer = ItemSerializer(items, many = True)
    return Response(Serializer.data)

@api_view(['POST'])
def addItem(request):
    Serializer = ItemSerializer(data=request.data)
    if Serializer.is_valid():
        Serializer.save()
    return Response(Serializer.data)