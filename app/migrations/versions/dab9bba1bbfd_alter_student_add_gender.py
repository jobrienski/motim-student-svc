"""alter_student_add_gender

Revision ID: dab9bba1bbfd
Revises: 57b96af32fb6
Create Date: 2022-11-14 14:55:53.166068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dab9bba1bbfd"
down_revision = "57b96af32fb6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("students", sa.Column("gender", sa.Text(), nullable=False, server_default="M"))


def downgrade() -> None:
    op.drop_column("students", "gender")
