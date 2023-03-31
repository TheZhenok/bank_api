import sqlalchemy as sa
import sqlalchemy_utils as sau
import datetime


metadata = sa.MetaData()

# Models
# 
roles = sa.Table(
    "roles",
    metadata,
    sa.Column("id", sa.Integer, autoincrement=True, primary_key=True, index=True),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("permissions", sa.JSON)
)

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, autoincrement=True, primary_key=True, index=True),
    sa.Column("email", sau.EmailType, nullable=False),
    sa.Column("password", sa.String),
    sa.Column("role_id", sa.ForeignKey("roles.id")),
    sa.Column("datetime_created", sa.TIMESTAMP, default=datetime.datetime.utcnow),
    sa.Column("datetime_deleted", sa.TIMESTAMP, nullable=True),
)
