"""empty message
Revision ID: 60c3cdeb752a
Revises: 3aa589b3bc53
Create Date: 2023-03-12 18:25:39.877162
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60c3cdeb752a'
down_revision = '3aa589b3bc53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.alter_column('description',
                              existing_type=sa.VARCHAR(length=250),
                              type_=sa.String(length=1000),
                              existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.alter_column('description',
                              existing_type=sa.String(length=1000),
                              type_=sa.VARCHAR(length=250),
                              existing_nullable=True)

    # ### end Alembic commands ###
