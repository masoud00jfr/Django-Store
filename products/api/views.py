from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Product
from .serializers import ProductSerializers


class ProductView(APIView):

    def get(self, request, format=None):
        response = dict()
        response['products'] = ProductSerializers(Product.objects.all(), many=True).data
        return Response(response)
