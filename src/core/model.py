import datetime
import decimal
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase): ...


class RoomTypeORM(Base):
    __tablename__='room_type'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    room_type_name: Mapped[str] = mapped_column(unique=True)

class ClientORM(Base):
    __tablename__='client'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    fullName: Mapped[str]
    adress: Mapped[str]
    phone_number: Mapped[str]
    bithday: Mapped[datetime.date]

class ServiceORM(Base):
    __tablename__='service'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    price: Mapped[decimal.Decimal]
    name: Mapped[str]

class BookingWithRoomORM(Base):
    __tablename__='booking_with_room'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    room_number: Mapped[int] = mapped_column(primary_key=True)

    arrivalDate: Mapped[datetime.date]
    departureDate: Mapped[datetime.date]
    numbersOfPeople: Mapped[int]
    room_cost: Mapped[decimal.Decimal]

    room_type_id: Mapped[int] = mapped_column(ForeignKey('room_type.id', ondelete='CASCADE'))

class OrderORM(Base):
    __tablename__='order'

    service_id: Mapped[int] = mapped_column(
        ForeignKey('service.id', ondelete='CASCADE'),
        primary_key=True, )
    
    client_id: Mapped[int] = mapped_column(
        ForeignKey('client.id', ondelete='CASCADE'),
        primary_key=True, )