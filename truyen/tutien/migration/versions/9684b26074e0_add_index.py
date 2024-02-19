"""add index

Revision ID: 9684b26074e0
Revises: ba7fbaae764c
Create Date: 2024-01-23 16:37:54.506328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9684b26074e0'
down_revision = 'ba7fbaae764c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_chapter_story_id'), 'chapter', ['story_id'], unique=False)
    op.create_index(op.f('ix_chapter_title'), 'chapter', ['title'], unique=False)
    op.create_index(op.f('ix_story_title'), 'story', ['title'], unique=False)
    op.drop_column('story', 'ausdfthor')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story', sa.Column('ausdfthor', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_story_title'), table_name='story')
    op.drop_index(op.f('ix_chapter_title'), table_name='chapter')
    op.drop_index(op.f('ix_chapter_story_id'), table_name='chapter')
    # ### end Alembic commands ###