"""Agregando tabla libro_diario

Revision ID: 7a2b0e499268
Revises: 460d0cd02e6b
Create Date: 2020-12-30 15:16:04.841621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a2b0e499268'
down_revision = '460d0cd02e6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libro__diario',
    sa.Column('id_libro_diario', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=200), nullable=False),
    sa.Column('descripcion', sa.String(length=200), nullable=True),
    sa.Column('id_user', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ondelete='set null'),
    sa.PrimaryKeyConstraint('id_libro_diario'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('libro__diario')
    # ### end Alembic commands ###