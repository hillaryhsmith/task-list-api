"""empty message

Revision ID: 03bab0df9159
Revises: 857b1327490e
Create Date: 2022-05-06 10:33:18.451688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03bab0df9159'
down_revision = '857b1327490e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'is_completed')
    # ### end Alembic commands ###
