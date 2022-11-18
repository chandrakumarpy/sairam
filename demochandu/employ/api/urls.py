from rest_framework import routers
from employ.api.views import EmployViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employ', EmployViewSet)
