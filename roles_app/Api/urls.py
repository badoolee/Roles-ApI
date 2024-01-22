from django.urls import path, include

from roles_app.Api.views import RolesList, RolesDetails

urlpatterns = [
    path("list/", RolesList.as_view(), name="roles-list"),
    path("<int:pk>/", RolesDetails.as_view(), name="roles-details"),
]
