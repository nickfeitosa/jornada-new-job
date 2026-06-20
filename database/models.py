from datetime import datetime

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class SelectionProcess(Base):
    __tablename__ = "selection_processes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    company: Mapped[str] = mapped_column(String(255))

    title: Mapped[str] = mapped_column(String(255))

    application_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    current_status: Mapped[str] = mapped_column(
        String(100),
        default="Candidatura enviada"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )