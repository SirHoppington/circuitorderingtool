"""empty message

Revision ID: 8209845d478c
Revises: 840cf22cfe5b
Create Date: 2022-03-31 14:58:25.377874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8209845d478c'
down_revision = '840cf22cfe5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('network_ref_associations',
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('quotation_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order_table.id'], ),
    sa.ForeignKeyConstraint(['provider_id'], ['provider_pricing.id'], ),
    sa.ForeignKeyConstraint(['quotation_id'], ['quotation.id'], ),
    sa.PrimaryKeyConstraint('provider_id', 'quotation_id', 'order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('network_ref_associations')
    op.drop_table('quotation')
    op.drop_table('provider_pricing')
    op.drop_table('order_table')
    # ### end Alembic commands ###
