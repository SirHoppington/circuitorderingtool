"""empty message

Revision ID: 97aea3eaa46e
Revises: 9ae41e2b6961
Create Date: 2022-03-28 14:21:24.195942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97aea3eaa46e'
down_revision = '9ae41e2b6961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provider_pricing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('supplier_ref', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quotation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('net', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('quote_table',
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('quotation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['provider_id'], ['provider_pricing.id'], ),
    sa.ForeignKeyConstraint(['quotation_id'], ['quotation.id'], ),
    sa.PrimaryKeyConstraint('provider_id', 'quotation_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote_table')
    op.drop_table('user')
    op.drop_table('quotation')
    op.drop_table('provider_pricing')
    # ### end Alembic commands ###