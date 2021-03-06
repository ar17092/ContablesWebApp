"""Agregando tabla partida_concepto hoy si xd

Revision ID: 923d825a9f29
Revises: 2f4947c9f608
Create Date: 2020-12-31 17:23:37.203398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '923d825a9f29'
down_revision = '2f4947c9f608'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partida_concepto',
    sa.Column('id_pconcepto', sa.Integer(), nullable=False),
    sa.Column('valor_parcial', sa.Float(), nullable=True),
    sa.Column('id_cuenta', sa.Integer(), nullable=True),
    sa.Column('id_partida', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cuenta'], ['cuenta.id_cuenta'], ondelete='set null'),
    sa.ForeignKeyConstraint(['id_partida'], ['partida.id_partida'], ondelete='set null'),
    sa.PrimaryKeyConstraint('id_pconcepto')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('partida_concepto')
    # ### end Alembic commands ###
