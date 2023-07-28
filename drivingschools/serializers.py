from rest_framework import serializers
from .models import DrivingPermission, DrivingSchool, DrivingSchoolSection

class DrivingSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingSchool
        fields = "__all__"

class DrivingPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingPermission
        fields = "__all__"

class DrivingSchoolSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingSchoolSection
        fields = "__all__"