"""Added products weights

Revision ID: 4a85393c261f
Revises: 714c36f18039
Create Date: 2023-08-05 19:40:51.348149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a85393c261f'
down_revision = '714c36f18039'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['product'], ['products.id'], ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('weights')
    # ### end Alembic commands ###
