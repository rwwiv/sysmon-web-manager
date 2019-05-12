import {Agent} from "@/types/agent";

export type Group = {
    name: string,
    sysmonVersion: string,
    configName: string,
    agents: Agent[]
}
