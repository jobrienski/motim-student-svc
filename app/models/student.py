from .meta import Base
import sqlalchemy_utils
import sqlalchemy as sa
from ..dto.student import StudentResponse


class StudentModel(Base):
    __tablename__ = "students"
    id = sa.Column(
        sqlalchemy_utils.types.uuid.UUIDType(),
        server_default=sa.text("gen_random_uuid()"),
        nullable=False,
        primary_key=True,
    )
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.text("statement_timestamp()"),
        nullable=False,
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.text("statement_timestamp()"),
        nullable=False,
    )
    deleted_at = sa.Column(sa.DateTime(timezone=True), nullable=True)
    first_name = sa.Column(sa.Text(), nullable=False)
    last_name = sa.Column(sa.Text(), nullable=False)
    date_of_birth = sa.Column(sa.Date(), nullable=False)
    number_of_classes = sa.Column(sa.Integer(), nullable=False)
    gender = sa.Column(sa.Text(), nullable=False)

    def to_student(self) -> StudentResponse:
        return StudentResponse(
            id=str(self.id),
            first_name=self.first_name,
            last_name=self.last_name,
            date_of_birth=self.date_of_birth,
            number_of_classes=self.number_of_classes,
            gender=self.gender,
        )
