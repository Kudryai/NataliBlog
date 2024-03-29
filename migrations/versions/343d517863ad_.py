"""empty message

Revision ID: 343d517863ad
Revises: 
Create Date: 2023-02-20 13:54:32.445938

"""
import flask_security
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "343d517863ad"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "lessons",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("date_lessons", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=True),
        sa.Column("slug", sa.String(length=140), nullable=True),
        sa.Column("body", sa.Text(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_table(
        "role",
        sa.Column(
            "update_datetime",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("permissions", sa.UnicodeText(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "tag",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("slug", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("last_login_ip", sa.String(length=64), nullable=True),
        sa.Column("current_login_ip", sa.String(length=64), nullable=True),
        sa.Column("tf_primary_method", sa.String(length=64), nullable=True),
        sa.Column("tf_totp_secret", sa.String(length=255), nullable=True),
        sa.Column("tf_phone_number", sa.String(length=128), nullable=True),
        sa.Column(
            "create_datetime",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_datetime",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("us_totp_secrets", sa.Text(), nullable=True),
        sa.Column("fs_webauthn_user_handle", sa.String(length=64), nullable=True),
        sa.Column(
            "mf_recovery_codes", flask_security.datastore.AsaList(), nullable=True
        ),
        sa.Column("us_phone_number", sa.String(length=128), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("username", sa.String(length=255), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("last_login_at", sa.DateTime(), nullable=True),
        sa.Column("current_login_at", sa.DateTime(), nullable=True),
        sa.Column("first_name", sa.String(length=100), nullable=True),
        sa.Column("pic_url", sa.String(length=100), nullable=True),
        sa.Column("last_name", sa.String(length=100), nullable=True),
        sa.Column("login_count", sa.Integer(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.Column("fs_uniquifier", sa.String(length=255), nullable=False),
        sa.Column("confirmed_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("fs_uniquifier"),
        sa.UniqueConstraint("fs_webauthn_user_handle"),
        sa.UniqueConstraint("us_phone_number"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "post_tags",
        sa.Column("post_id", sa.Integer(), nullable=True),
        sa.Column("tag_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["post.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tag.id"],
        ),
    )
    op.create_table(
        "roles_users",
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
    )
    op.create_table(
        "user_lessons",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("lessons_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["lessons_id"],
            ["lessons.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "lessons_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_lessons")
    op.drop_table("roles_users")
    op.drop_table("post_tags")
    op.drop_table("user")
    op.drop_table("tag")
    op.drop_table("role")
    op.drop_table("post")
    op.drop_table("lessons")
    # ### end Alembic commands ###
