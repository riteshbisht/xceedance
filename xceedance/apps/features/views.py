from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from features.serializers import ClientSerializer, FeatureSerializer

from features.models import Feature, Client


class ClientApiView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
# Create your views here.


class ClientDetailApiView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class FeatureApiView(ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class FeatureDetailApiView(RetrieveUpdateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
