from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import (
    RoomTypeORM
)

from .schema import (
    RoomTypeCreateSchema,
    RoomTypeUpdateSchema
)

# room type cruds
async def get_room_types(session: AsyncSession) ->[RoomTypeORM]:
    stmt = select(RoomTypeORM).order_by(RoomTypeORM.id)
    result: Result = await session.execute(stmt)
    room_types = result.scalars().all()
    return list(room_types)

async def get_room_type(
        session: AsyncSession, 
        room_type_id: int
        ) -> RoomTypeORM | None:
    return await session.get(RoomTypeORM, room_type_id)

async def create_room_type(
        session: AsyncSession, 
        room_type_in: RoomTypeCreateSchema
        ) -> RoomTypeORM:
    result = RoomTypeORM(**room_type_in.model_dump())
    session.add(result)
    await session.commit()
    return result

async def update_room_type(
        session: AsyncSession, 
        room_type: RoomTypeORM, 
        room_type_update: RoomTypeUpdateSchema,
        partial: bool = False,
        ) -> RoomTypeORM:
    for name, value in room_type_update.model_dump(exclude_unset=partial).items():
        setattr(room_type, name, value)
    await session.commit()
    return room_type

async def delete_room_type(
        session: AsyncSession,
        room_type: RoomTypeORM
) -> None:
    await session.delete(room_type)
    await session.commit()