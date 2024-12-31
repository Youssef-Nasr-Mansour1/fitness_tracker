from rest_framework import serializers
from .models import CustomUser
from .models import Activity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'profile_picture', 'bio')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'activity_type', 'duration', 'distance', 'calories_burned', 'date')
