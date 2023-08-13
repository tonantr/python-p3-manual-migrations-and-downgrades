"""Renaming students to scholars

Revision ID: 8eb524b8ce9e
Revises: 791279dd0760
Create Date: 2023-08-13 16:12:09.284806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eb524b8ce9e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
