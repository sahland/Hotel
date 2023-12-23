from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from core.model import RoomTypeORM

from . import crud as crud_room_type

async def room_type_by_id(
    room_type_id: Annotated[int, Path], 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ) -> RoomTypeORM:
    room_type = await crud_room_type.get_room_type(session=session, room_type_id=room_type_id)
    if room_type is not None:
        return room_type
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Room Type form with {room_type_id} id not found!'
    )