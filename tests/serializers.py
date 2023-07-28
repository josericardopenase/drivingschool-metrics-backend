# serializers.py
from rest_framework import serializers
from .models import TestCenter, TestType, Test

class TestCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCenter
        fields = '__all__'

class TestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestType
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    num_suspensos = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = '__all__'

    def get_num_suspensos(self, obj):
        return obj.num_presentados - obj.num_aptos
