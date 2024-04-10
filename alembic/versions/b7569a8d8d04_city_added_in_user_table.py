"""city added in user table

Revision ID: b7569a8d8d04
Revises: 7ef2e6eb8c16
Create Date: 2024-04-10 13:36:25.480234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7569a8d8d04'
down_revision: Union[str, None] = '7ef2e6eb8c16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('city', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'city')
    # ### end Alembic commands ###