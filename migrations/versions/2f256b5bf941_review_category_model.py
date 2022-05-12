"""review category model

Revision ID: 2f256b5bf941
Revises: 
Create Date: 2022-05-12 03:51:39.750803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f256b5bf941'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pitch_category_fkey', 'pitch', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('pitch_category_fkey', 'pitch', 'category', ['category'], ['id'])
    # ### end Alembic commands ###
