from datetime import datetime
from sqlalchemy import DATETIME, Column, Integer, String, DECIMAL
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotion"

    id = Column(Integer, primary_key=True, nullable=False, index=True, autoincrement=True)
    code = Column(String(255))
    discount = Column(DECIMAL(4, 2))
    expiration = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
