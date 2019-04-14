from django.contrib.auth import authenticate
from django.db.models import Q
from pytz import unicode
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from datetime import datetime


@api_view(['post'])
def update_parking(request):

    if request.method == 'POST':

        parking = SmartpParkinglot.objects.all().get(id=request.data.get('id'))

        if parking is not None:
            # if check_password(request.data.get('password'), 'password'):
            parking.actualparkedcars = request.data.get('actualparkedcars')
            parking.save()

            history = {
                'parkedcars': request.data.get('actualparkedcars'),
                'date': request.data.get('date'),
                'parkinglot': request.data.get('id'),
            }

            serializer = OldCapacitySerializer(data=history)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(request, status=status.HTTP_404_NOT_FOUND)
