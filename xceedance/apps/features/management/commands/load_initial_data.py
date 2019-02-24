from django.core.management.base import BaseCommand

from features.models import Client

class Command(BaseCommand):
    """
    Custom command to Update course catalogue list in cache.
    """
    help = 'Update course catalogue in cache'

    def handle(self, *args, **options):
        names = ['Client A', 'Client B', 'Client C']
        clients = []
        for name in names:
            clients.append(Client(name=name))

        Client.objects.bulk_create(clients)
