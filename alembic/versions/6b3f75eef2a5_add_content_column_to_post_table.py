"""add content column to post table

Revision ID: 6b3f75eef2a5
Revises: 32aa748d40a8
Create Date: 2025-08-27 20:49:25.208491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b3f75eef2a5'
down_revision: Union[str, Sequence[str], None] = '32aa748d40a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
