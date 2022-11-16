# app/controllers/student_controller.py

from fastapi import APIRouter, Body, Depends, Path

from ..dto.student import CreateStudent, StudentResponse
from ..processors.student_processor import StudentProcessor


router = APIRouter()


class StudentControllerParams:
    def __init__(self, student_processor=Depends(StudentProcessor)):
        self.student_processor = student_processor


@router.post(
    "/",
    response_model=StudentResponse,
    tags=["student"],
)
def create_student(
    create_student_input: CreateStudent = Body(...),
    sp: StudentControllerParams = Depends(),
):
    return sp.student_processor.create_student(create_student_input)


@router.get(
    "/{id}",
    response_model=StudentResponse,
)
def get_student_by_id(
    id: str = Path(..., min_length=1), sp: StudentControllerParams = Depends()
):
    return sp.student_processor.find_student_by_id(id)
