from pydantic import BaseModel, ConfigDict

# RoomType schemas
class RoomTypeBaseSchema(BaseModel):
    room_type_name: str

class RoomTypeCreateSchema(RoomTypeBaseSchema): ...

class RoomTypeUpdateSchema(RoomTypeBaseSchema): ...

class RoomTypeSchema(RoomTypeBaseSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)