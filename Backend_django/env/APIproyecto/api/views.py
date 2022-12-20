
from .models import Becas
from .serializers import BecasSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class BecasViewSet(viewsets.ModelViewSet):
    queryset = Becas.objects.all()
    serializer_class = BecasSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'porcentaje': ['gte'],
        'pais': ['istartswith']
    }

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer








   
