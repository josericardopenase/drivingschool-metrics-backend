import { service } from "../../service"

interface DrivingSchoolSection{
    id : number,
    code:  string,
    driving_school : string
    name : string
}

export const DrivingSchoolSectionsService = service.createService<DrivingSchoolSection>(['drivingschool'], "/driving/sections/")