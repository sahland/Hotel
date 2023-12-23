from fastapi import APIRouter

from .route import RoomTypeRouter

room_type = RoomTypeRouter()
router = APIRouter()

router.include_router(router=room_type.router, prefix='/room-type')