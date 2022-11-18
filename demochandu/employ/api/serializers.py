from rest_framework import  serializers
from employ.models import Employ
from django.contrib.auth.models import User

# Serializers define the API representation.
class EmploySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employ
        fields = ['url', 'first_name', 'last_name', 'date_of_birth', 'gender']
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']