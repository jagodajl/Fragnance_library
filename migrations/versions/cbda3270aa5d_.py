"""empty message

Revision ID: cbda3270aa5d
Revises: 
Create Date: 2022-09-01 21:46:46.446439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbda3270aa5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('surname', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_brand_name'), 'brand', ['name'], unique=False)
    op.create_index(op.f('ix_brand_surname'), 'brand', ['surname'], unique=False)
    op.create_table('fragnance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fragnance_name'), 'fragnance', ['name'], unique=False)
    op.create_index(op.f('ix_fragnance_price'), 'fragnance', ['price'], unique=False)
    op.create_index(op.f('ix_fragnance_year'), 'fragnance', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fragnance_year'), table_name='fragnance')
    op.drop_index(op.f('ix_fragnance_price'), table_name='fragnance')
    op.drop_index(op.f('ix_fragnance_name'), table_name='fragnance')
    op.drop_table('fragnance')
    op.drop_index(op.f('ix_brand_surname'), table_name='brand')
    op.drop_index(op.f('ix_brand_name'), table_name='brand')
    op.drop_table('brand')
    # ### end Alembic commands ###