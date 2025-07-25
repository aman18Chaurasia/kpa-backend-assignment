from pydantic import BaseModel

class BogieFormCreate(BaseModel):
    name: str
    part_number: str

class WheelFormCreate(BaseModel):
    inspector_name: str
    wheel_number: str
