from rest_framework import serializers

from business.serializers import DrivingLicenseSerializer
from code_utils.serializers import Base64ImageField
from vehicle_fleet.models import FuelType, Vehicle


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields='__all__'

class VehicleGetSerializer(serializers.ModelSerializer):
    driving_license = DrivingLicenseSerializer(read_only=True)
    fuel_type = FuelTypeSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields='__all__'

class VehiclePostSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Vehicle
        exclude = ['insurance_payment_date', 'registration_date', 'vehicle_circulation_permission_document', 'technical_data_sheet_document', 'insurance_document', 'itv_document', 'is_active']
