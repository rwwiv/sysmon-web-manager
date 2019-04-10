from heartbeat.models import Group, Sysmon, Configuration


def create_group(name, json):
    try:
        group = Group.objects.get(NAME=name)
        return -1
        
    except Exception as e:
        try:
            sysmon = Sysmon.objects.get(VERSION = json['sysmon_version'])
            try:
                config = Configuration.objects.get(NAME = json['configuration'])
                new_group = Group(NAME = name,
                                  CONFIGURATION = config,
                                  SYSMON = sysmon)
                new_group.save()
                return 1
            except Exception as e:
                return -1
        except Exception as e:
            return -1