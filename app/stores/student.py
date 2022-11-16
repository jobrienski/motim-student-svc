from fastapi import Depends
from sqlalchemy.orm import Session

from ..dto.student import CreateStudent
from ..models.student import StudentModel
from ..lib.server.db import get_db


class StudentStore:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_student(self, ct: CreateStudent) -> StudentModel:
        new_student_model = StudentModel(
            first_name=ct.first_name,
            last_name=ct.last_name,
            date_of_birth=ct.date_of_birth,
            number_of_classes=ct.number_of_classes,
            gender=ct.gender,
        )
        self.db.add(new_student_model)
        self.db.commit()
        self.db.refresh(new_student_model)
        return new_student_model

    def find_student_by_id(self, id: str) -> StudentModel:
        return self.db.query(StudentModel).filter(StudentModel.id == id).one()
