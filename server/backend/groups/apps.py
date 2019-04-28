from django.apps import AppConfig
from models.models import Group


class GroupsConfig(AppConfig):
    name = 'groups'

    def ready(self):
        if not Group.objects.exists(NAME='no_group'):
            Group(NAME='no_group').save()
