from sqlalchemy import Column, VARCHAR, BOOLEAN
from sqlalchemy.dialects.postgresql import BYTEA

from db.models.base import BaseModel


class DBUser(BaseModel):

    __tablename__ = "user"

    login = Column(VARCHAR(20), unique=True, nullable=False)
    password = Column(BYTEA(), nullable=False)
    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    is_delete = Column(BOOLEAN(), nullable=False, default=False)
