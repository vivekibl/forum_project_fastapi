"""add image field in post

Revision ID: 33c5bc4d23e1
Revises: 0c4d18155a27
Create Date: 2021-11-16 11:38:42.925929

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '33c5bc4d23e1'
down_revision = '0c4d18155a27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('forum_id', sa.Integer(), nullable=True))
    op.add_column('posts', sa.Column('prefix', sa.String(), nullable=True))
    op.add_column('posts', sa.Column('topic_file', sqlalchemy_utils.types.url.URLType(), nullable=True))
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('posts', 'content',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_foreign_key(None, 'posts', 'forums', ['forum_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.alter_column('posts', 'content',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('posts', 'topic_file')
    op.drop_column('posts', 'prefix')
    op.drop_column('posts', 'forum_id')
    # ### end Alembic commands ###