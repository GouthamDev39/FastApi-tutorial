"""Create post table

Revision ID: 126f1a3558cf
Revises: 
Create Date: 2024-06-01 08:38:00.695486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '126f1a3558cf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable= False, primary_key= True), 
                    sa.Column('title', sa.Integer(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
