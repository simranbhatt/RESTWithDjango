"""Model serializers are necessary because the Response object cannot natively handle complex data types like Django objects"""

from rest_framework import serializers
from base.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'