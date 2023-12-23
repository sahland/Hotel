from fastapi import APIRouter, status, Depends
from fastapi_pagination import Page, Params, paginate
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper

from . import crud
from .dependencie import room_type_by_id
from .schema import RoomTypeSchema, RoomTypeCreateSchema, RoomTypeUpdateSchema


class RoomTypeRouter:
    router = APIRouter(tags=['Room Type'])    

    @router.get('/', response_model=Page[RoomTypeSchema])
    async def get_room_types(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
        ):
        return paginate(await crud.get_room_types(session=session))

    @router.get('/{room_type_id}', response_model=RoomTypeSchema)
    async def get_room_type(
        room_type: RoomTypeSchema = Depends(room_type_by_id)
        ):
        return room_type
    
    @router.post('/', response_model=RoomTypeSchema,
             status_code=status.HTTP_201_CREATED)
    async def create_room_type(
    room_type_in: RoomTypeCreateSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ):
        return await crud.create_room_type(session=session, room_type_in=room_type_in)

    @router.put('/{room_type_id}')
    async def update_room_type(
    room_type_update: RoomTypeUpdateSchema,
    room_type: RoomTypeSchema = Depends(room_type_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ):
        return await crud.update_room_type(
            session=session,
            room_type=room_type,
            room_type_update=room_type_update
        )

    @router.delete('/{room_type_id}', status_code=status.HTTP_204_NO_CONTENT)
    async def delete_release_form(
        room_type: RoomTypeSchema = Depends(room_type_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ) -> None:
        await crud.delete_room_type(session=session, room_type=room_type)
    
