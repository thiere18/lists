from typing import Text
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class List(Base):
    __tablename__ ='lists'
    id = Column(Integer,nullable=False,primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True) , nullable=False, server_default=text('now()'))

