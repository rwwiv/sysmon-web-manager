from heartbeat.models import Group, Sysmon, Configuration


def create_group(name, json):
    try:
        group = Group.objects.get(NAME=name)
        try:
            sysmon = Sysmon.objects.get(VERSION = json['sysmon_version']).VERSION
            try:
                config = Configuration.objects.get(NAME = json['configuration']).NAME
                new_group = Group(NAME = name,
                                  CONFIGURATION = config,
                                  SYSMON = sysmon)
                return 1
            except Exception as e:
                return -1
        except Exception as e:
            return -1
        
    except Exception as e:
        return -1