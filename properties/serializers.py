from rest_framework import serializers
from .models import Owner, Property, Feedback

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Property
        fields = '__all__'

    def validate_address(self, value):
        """
        Custom validation to ensure that the address is unique.
        """
        if Property.objects.filter(address=value).exists():
            raise serializers.ValidationError("A property with this address already exists.")
        return value

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
