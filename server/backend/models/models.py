from django.db import models


class User(models.Model):
    USER_ID = models.CharField(max_length=200, primary_key=True)
    PASSWORD = models.CharField(max_length=200)
    LAST_LOGGED_IN = models.CharField(max_length=200)
    LAST_LOGGED_OUT = models.CharField(max_length=200)


class Configuration(models.Model):
    NAME = models.CharField(max_length=200, primary_key=True)
    IS_DEFAULT = models.BooleanField()


class Sysmon(models.Model):
    VERSION = models.CharField(max_length=200, primary_key=True)
    IS_CURRENT = models.BooleanField()


class Group(models.Model):
    NAME = models.CharField(max_length=200, primary_key=True)
    CONFIGURATION = models.ForeignKey(Configuration, on_delete=models.SET_NULL, null=True)
    SYSMON = models.ForeignKey(Sysmon, on_delete=models.SET_NULL, null=True)


class Agent(models.Model):
    UUID = models.CharField(max_length=200, primary_key=True)
    IP_ADDRESS = models.CharField(max_length=200)
    ONLINE = models.BooleanField()
    SYSMON_VERSION_CURRENT = models.CharField(max_length=200)
    SYSMON_VERSION_NEW = models.CharField(max_length=200)
    CONFIG_NAME_CURRENT = models.CharField(max_length=200)
    CONFIG_NAME_NEW = models.CharField(max_length=200)
    EXEC_LAST_RUNNING_AT = models.CharField(max_length=200, blank=True, null=True)
    EXEC_RUNNING = models.BooleanField()
    NEEDS_UNINSTALL = models.BooleanField()
    NEEDS_RESTART = models.BooleanField()
    NEEDS_INSTALL = models.BooleanField()
    ATTEMPTED_INSTALL = models.BooleanField()
    GROUP = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Global_Variables(models.Model):
    VARIABLE_TYPE = models.CharField(max_length=100, primary_key=True)
    VARIABLE_VALUE = models.CharField(max_length=500)
