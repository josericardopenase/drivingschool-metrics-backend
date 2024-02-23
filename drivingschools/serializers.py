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
    name = serializers.SerializerMethodField('name')

    class Meta:
        model = DrivingSchoolSection
        fields = ("name", "code", "driving_school", "id")
    
    def name(self, obj):
        return obj.name

    
    