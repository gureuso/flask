"""empty message

Revision ID: aea3cd67dbbe
Revises: 
Create Date: 2020-07-01 23:31:40.497053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aea3cd67dbbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_tests',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.String(120)),
    )
    op.create_table(
        'tests',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('message', sa.String(120)),
    )


def downgrade():
    op.drop_table('test_tests')
    op.drop_table('tests')
