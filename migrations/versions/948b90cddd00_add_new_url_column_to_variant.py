"""Add new url column to Variant

Revision ID: 948b90cddd00
Revises: 8a63890141c8
Create Date: 2025-01-15 16:05:42.867908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '948b90cddd00'
down_revision = '8a63890141c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('variants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('variants', schema=None) as batch_op:
        batch_op.drop_column('url')

    # ### end Alembic commands ###