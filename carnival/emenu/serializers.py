from emenu.models import Vendor
from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']