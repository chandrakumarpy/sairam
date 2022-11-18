from django.contrib.auth.models import User
from employ.models import Employ
from rest_framework import  viewsets
from employ.api.serializers import EmploySerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated



class EmployViewSet(viewsets.ModelViewSet):

    queryset = Employ.objects.all()
    serializer_class = EmploySerializer
    permission_classes = [IsAuthenticated]
    


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
