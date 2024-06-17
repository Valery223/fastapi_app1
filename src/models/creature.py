from db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Creature(Base):
    __tablename__ = "creature"

    name: Mapped[str] = mapped_column(primary_key=True)
    country: Mapped[str]
    area: Mapped[str]
    description: Mapped[str]
    aka: Mapped[str]