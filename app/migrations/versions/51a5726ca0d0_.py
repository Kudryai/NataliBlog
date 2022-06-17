"""empty message

Revision ID: 51a5726ca0d0
Revises: 
Create Date: 2022-06-16 12:46:26.813629

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '51a5726ca0d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('slug', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(collation='utf8_unicode_ci', length=150), nullable=True),
    sa.Column('slug', mysql.VARCHAR(collation='utf8_unicode_ci', length=140), nullable=True),
    sa.Column('body', mysql.TEXT(collation='utf8_unicode_ci'), nullable=True),
    sa.Column('created', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('slug', 'post', ['slug'], unique=False)
    # ### end Alembic commands ###