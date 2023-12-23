"""Create order table

Revision ID: 54cda57fa654
Revises: ca393f5cc40d
Create Date: 2023-12-23 22:55:07.915951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54cda57fa654'
down_revision: Union[str, None] = 'ca393f5cc40d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('service_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('service_id', 'client_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###