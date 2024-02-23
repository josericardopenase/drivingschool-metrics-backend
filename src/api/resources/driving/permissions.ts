import { service } from "../../service"

export interface DrivingSchoolPermission{
    id : number,
    name:  string,
}

export const PermissionServices = service.createService<DrivingSchoolPermission>(['perimssions'], "/driving/permissions/", {
    retry: 1, retryDelay: 3000, retryOnMount: false, refetchOnReconnect: false, refetchOnWindowFocus: false, refetchIntervalInBackground: false
})