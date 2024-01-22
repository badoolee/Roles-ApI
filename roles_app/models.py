from django.db import models

from user_app.models import User


class RolesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
