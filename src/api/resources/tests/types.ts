import { service } from "../../service"

interface TestType{
    id : number,
    name : string
}

export const TestTypeService = service.createService<TestType>(['test_types'], "/tests/types/")