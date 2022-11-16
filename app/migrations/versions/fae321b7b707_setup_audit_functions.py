"""setup_audit_functions

Revision ID: fae321b7b707
Revises:
Create Date: 2022-11-14 13:50:13.235394

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "fae321b7b707"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    CREATE EXTENSION IF NOT EXISTS "pgcrypto";

    CREATE OR REPLACE FUNCTION update_modified_date()
    RETURNS TRIGGER AS $$
    BEGIN
      NEW.updated_at = statement_timestamp();
      NEW.created_at = OLD.created_at;
      NEW.id = OLD.id;
      RETURN NEW;
    END;
    $$ LANGUAGE 'plpgsql';

    CREATE OR REPLACE FUNCTION soft_delete()
    RETURNS TRIGGER AS $$
    BEGIN
      EXECUTE format('UPDATE %I SET deleted_at = statement_timestamp() WHERE id = $1', TG_TABLE_NAME) USING OLD.id;
      RETURN NULL;
    END;
    $$ LANGUAGE 'plpgsql';
    """
    )


def downgrade():
    op.execute(
        """
      DROP FUNCTION soft_delete();
      DROP FUNCTION update_modified_date();
      DROP EXTENSION "pgcrypto";
      """
    )
