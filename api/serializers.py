from rest_framework import serializers, status
from .models import Rating,Phone

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'name', 'description','nbr_of_rating','avr_of_rating')
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'phone', 'user', 'stars')        