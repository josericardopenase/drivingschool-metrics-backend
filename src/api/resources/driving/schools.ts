import { service } from "../../service"

interface DrivingSchool{
    id : number,
    code:  string,
    name : string
}

export const DrivingSchoolService = service.createService<DrivingSchool>(['drivingschool'], "/driving/schools/")