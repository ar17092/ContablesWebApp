"""Agregando tabla partida

Revision ID: 3d14f784336b
Revises: f747da15f31b
Create Date: 2020-12-30 20:02:48.095861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d14f784336b'
down_revision = 'f747da15f31b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partida',
    sa.Column('id_partida', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=200), nullable=False),
    sa.Column('valor_debe', sa.Float(), nullable=True),
    sa.Column('valor_haber', sa.Float(), nullable=True),
    sa.Column('id_ldiario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_ldiario'], ['libro__diario.id_libro_diario'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id_partida')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('partida')
    # ### end Alembic commands ###