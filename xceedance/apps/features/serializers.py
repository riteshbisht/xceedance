from rest_framework import serializers
from features.models import Feature, Client
from django.db.models.fields import DateField
from django.conf import settings
from datetime import datetime

class FeatureSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Feature
        fields = ('title','description', 'status', 'client', 'client_name' ,'priority', 'target_date', 'product', 'product_name')

    def get_status(self, obj):
        return obj.get_status_display()

    def get_client_name(self, obj):
        return obj.client.name

    def get_product_name(self, obj):
        return obj.get_product_display()

    def validate_target_date(self, value):
        if value < datetime.now().date():
            raise serializers.ValidationError('Date cannot be in the past')  
        return value

    def validate_priority(self, value):
        if not value:
            raise serializers.ValidationError('Priority is Required')  
        return value


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
