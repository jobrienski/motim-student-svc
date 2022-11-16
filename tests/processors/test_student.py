import datetime

from unittest.mock import patch
from app.dto.student import CreateStudent
from app.models import StudentModel
from app.stores.student import StudentStore
from app.processors.student_processor import StudentProcessor

student_store = StudentStore()
student_processor = StudentProcessor(student_store)

expected_created_student = StudentModel(
    id="123",
    first_name="test_first",
    last_name="test_last",
    gender="M",
    number_of_classes=3,
    date_of_birth=datetime.date.fromisocalendar(2005, 1, 1),
)


@patch.object(
    student_store,
    "create_student",
    return_value=expected_created_student,
)
def test_create_student(*_):
    createStudentReq = CreateStudent(
        first_name=expected_created_student.first_name,
        last_name=expected_created_student.last_name,
        date_of_birth=expected_created_student.date_of_birth,
        number_of_classes=expected_created_student.number_of_classes,
        gender=expected_created_student.gender,
    )
    student = student_processor.create_student(createStudentReq)
    assert student.id == expected_created_student.id
    assert student.first_name == expected_created_student.first_name
    assert student.last_name == expected_created_student.last_name
    assert student.number_of_classes == expected_created_student.number_of_classes
    assert student.gender == expected_created_student.gender
    assert student.date_of_birth == expected_created_student.date_of_birth
