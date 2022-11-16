# app/dto/student.py
from datetime import date

from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=255, description="first name")
    last_name: str = Field(..., min_length=2, max_length=255, description="last name")
    date_of_birth: date = Field(..., description="Date of birth")
    gender: str = Field(..., regex="^[MF]", description="M or F")
    number_of_classes: int = Field(..., gt=0, description="number of classes")

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jim",
                "last_name": "OB",
                "date_of_birth": "1985-05-05",
                "number_of_classes": 10,
                "gender": "M",
            }
        }


class CreateStudent(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: str = Field(..., description="the student id (uuid)")
