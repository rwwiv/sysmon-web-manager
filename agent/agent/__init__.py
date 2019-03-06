import time
import win32serviceutil
import win32service
import win32event
import servicemanager

import bg_process

from agent_config import env_config, env_config_file, user_config


class SysMonagerAgentService(win32serviceutil.ServiceFramework):
    _svc_name_ = env_config['agent']['service_name']
    _svc_display_name_ = env_config['agent']['display_name']

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            bg_process.run()
            rc = win32event.WaitForSingleObject(self.hWaitStop, 1000 * 60)  # wait for Stop command sent to service


if __name__ == "__main__":
    while True:
        bg_process.run()
        time.sleep(30)

    # if len(sys.argv) == 0:
    #     servicemanager.Initialize()
    #     servicemanager.PrepareToHostSingle(SysMonagerAgentService)
    #     servicemanager.StartServiceCtrlDispatcher()
    # else:
    #     win32serviceutil.HandleCommandLine(SysMonagerAgentService)
