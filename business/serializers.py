from rest_framework import serializers

from business.models import Section, DrivingLicense
from code_utils.serializers import Base64ImageField


class SectionSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Section
        fields = '__all__'

class DrivingLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingLicense
        fields = '__all__'