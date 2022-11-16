# app/processors/student_processor.py
from fastapi import Depends

from ..dto.student import CreateStudent, StudentResponse
from ..stores.student import StudentStore


class StudentProcessor:
    def __init__(self, student_store=Depends(StudentStore)):
        self.student_store = student_store

    def create_student(self, student_info: CreateStudent) -> StudentResponse:
        return self.student_store.create_student(student_info).to_student()

    def find_student_by_id(self, id: str) -> StudentResponse:
        return self.student_store.find_student_by_id(id).to_student()
