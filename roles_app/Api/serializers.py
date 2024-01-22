from rest_framework import serializers
from roles_app.models import RolesModel


class RolesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RolesModel
        fields = "__all__"
