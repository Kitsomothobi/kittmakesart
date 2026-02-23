from sqlalchemy import Column, Integer, String, Text
from database import Base

class Commission(Base):
    __tablename__ = "commissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    type = Column(String(100), nullable=False)
    budget = Column(String(100), nullable=True)
    description = Column(Text, nullable=False)


