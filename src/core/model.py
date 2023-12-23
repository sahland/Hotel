from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase): ...


class RoomTypeORM(Base):
    __tablename__='room_type'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    room_type_name: Mapped[str] = mapped_column(unique=True)