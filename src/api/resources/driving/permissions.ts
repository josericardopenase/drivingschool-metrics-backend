import { service } from "../../service"

interface DrivingSchool{
    id : number,
    name:  string,
}

export const PermissionServices = service.createService<DrivingSchool>(['perimssions'], "/driving/permissions/")