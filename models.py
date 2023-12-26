from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from databases import Base

class tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(Boolean, default=False)