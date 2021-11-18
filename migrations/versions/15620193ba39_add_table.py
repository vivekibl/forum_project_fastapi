"""add  table

Revision ID: 15620193ba39
Revises: 642ceef418b6
Create Date: 2021-11-15 17:56:19.678603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15620193ba39'
down_revision = '642ceef418b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('tags_id', sa.Integer(), nullable=False),
    sa.Column('posts.id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posts.id'], ['tags.id'], ),
    sa.ForeignKeyConstraint(['tags_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('tags_id', 'posts.id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('forums')
    op.drop_table('tags')
    # ### end Alembic commands ###
