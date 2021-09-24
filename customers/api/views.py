from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegisterSerializer


@api_view(['POST', ])
def register_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new customer'
            data['first_name'] = account.first_name
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            return serializer.errors
        return Response(data)
