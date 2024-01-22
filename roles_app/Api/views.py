from rest_framework import generics

from roles_app.Api.serializers import RolesSerializer
from roles_app.models import RolesModel
from roles_app.Api.permissions import IsAdminOrReadOnly


class RolesList(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = RolesModel.objects.all()
    serializer_class = RolesSerializer


class RolesDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = RolesModel.objects.all()
    serializer_class = RolesSerializer
