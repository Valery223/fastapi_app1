from ...src.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Explorer(Base):
    __tablename__ = "explorer"

    name: Mapped[str] = mapped_column(primary_key=True)
    country: Mapped[str]
    description: Mapped[str]