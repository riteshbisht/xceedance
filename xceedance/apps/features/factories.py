
import factory
from features.models import *
from datetime import datetime

class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    name = "Client name "


class FeatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Feature

    title = 'this is first'
    description = 'this is descriptioj'
    status = 0
    last_status = 0
    priority = 1
    target_date = datetime(year=2019, month=2, day=28)
    client =  factory.SubFactory(ClientFactory)
    product = 1


