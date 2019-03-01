from django.db import models


class Agent(models.Model):
    UUID = models.CharField(max_length=200)
    IP_ADDRESS = models.CharField(max_length=200)
    ONLINE = models.BooleanField()
    SYSMON_VERSION_CURRENT = models.CharField(max_length=200)
    SYSMON_VERSION_NEW = models.CharField(max_length=200)
    CONFIG_NAME_CURRENT = models.CharField(max_length=200)
    CONFIG_NAME_NEW = models.CharField(max_length=200)
    EXEC_LAST_RUNNING_AT = models.CharField(max_length=200)
    EXEC_RUNNING = models.BooleanField()
    NEEDS_UNINSTALL = models.BooleanField()
    NEEDS_RESTART = models.BooleanField()
    NEEDS_INSTALL = models.BooleanField()


class User(models.Model):
    USER_ID = models.CharField(max_length=200)
    PASSWORD = models.CharField(max_length=200)
    LAST_LOGGED_IN = models.CharField(max_length=200)
    LAST_LOGGED_OUT = models.CharField(max_length=200)


class Configuration(models.Model):
    NAME = models.CharField(max_length=200)
    IS_DEFAULT = models.BooleanField()

class Sysmon(models.Model):
    NAME = models.CharField(max_length=200)
    IS_CURRENT = models.BooleanField()