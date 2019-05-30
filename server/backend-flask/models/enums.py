import enum


class StatusTypes(enum.Enum):
    OFFLINE = 'Offline'
    ONLINE = 'Online'
    UNAVAILABLE = "Unavailable"
    NEW = 'Uninitialized'


class ActionTypes(enum.Enum):
    INSTALL = 'install'
    UNINSTALL = 'uninstall'
    RESTART = 'restart'
    UPDATE = 'update'


class ExternalLinks(enum.Enum):
    SYSMON_VERSION_TRACKING_REPO = 'tracking_repo'
    SYSMON_DOWNLOAD_URL = 'download_url'
