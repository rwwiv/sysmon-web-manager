from django.db import models

class agent(models.Model):
    UUID = models.CharField(max_length=200)
    IPV4_ADDRESS = models.CharField(max_length=200)
    IPV6_ADDRESS = models.CharField(max_length=200)
    ONLINE = models.BooleanField()
    SYSMON_VERSION_CURRENT = models.CharField(max_length=200)
    SYSMON_VERSION_NEW = models.CharField(max_length=200)
    CONFIG_NAME_CURRENT = models.CharField(max_length=200)
    CONFIG_NAME_NEW = models.CharField(max_length=200)
    EXEC_RUNNING = models.BooleanField()

class user(models.Model):
    USER_ID = models.CharField(max_length=200)
    PASSWORD = models.CharField(max_length=200)
    LAST_LOGGED_IN = models.CharField(max_length=200)
    LAST_LOGGED_OUT = models.CharField(max_length=200)
