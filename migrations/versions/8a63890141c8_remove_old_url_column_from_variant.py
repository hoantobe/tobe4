"""Remove old url column from Variant

Revision ID: 8a63890141c8
Revises: eec916ab5077
Create Date: 2025-01-15 15:58:20.201722

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8a63890141c8'
down_revision = 'eec916ab5077'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('variants', schema=None) as batch_op:
        batch_op.drop_column('url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('variants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', mysql.TEXT(), nullable=True))

    # ### end Alembic commands ###
