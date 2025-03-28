from rest_framework import serializers
from .models import ServiceRequest

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['id', 'request_type', 'description', 'status', 'created_at', 'user']
        read_only_fields = ["created_at", "updated_at", "user"]

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if 'status' in validated_data and not (request and request.user and request.user.is_staff):
            raise serializers.ValidationError({"status": "Only admins can update the status."})
        
        return super().update(instance, validated_data)
