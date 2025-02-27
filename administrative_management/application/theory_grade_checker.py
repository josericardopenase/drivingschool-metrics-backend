from abc import ABC, abstractmethod
from pydantic import BaseModel, ValidationError

class GradeResponse(BaseModel):
    calification: str
    errors: str

class TheoryGradeCheckerInterface(ABC):
    @abstractmethod
    def fetch_grade(self, DNI: str, fechaExamen: str, clasePermiso: str, nacimiento: str) -> GradeResponse:
        pass
