"""empty message

Revision ID: 93e409dafa6b
Revises: e5d367fd871f
Create Date: 2021-10-27 20:02:56.476480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93e409dafa6b'
down_revision = 'e5d367fd871f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_category')
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('category_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='category_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('product_category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='product_category_category_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='product_category_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_category_pkey')
    )
    # ### end Alembic commands ###
