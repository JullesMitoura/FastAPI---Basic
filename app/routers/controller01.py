from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


router = APIRouter(prefix="/controller01", tags=["controller01"])

class Controller01Response(BaseModel):
    id: int
    value: str

class Controller01Request(BaseModel):
    id: int
    value: str

@router.get("/", response_model=List[Controller01Response])
def list_values() -> List:
    return [Controller01Response(id=1, value="value01"), 
            Controller01Response(id=2, value="value02")
        ]


@router.post("/", response_model=Controller01Response, status_code=201)
def new_values(value: Controller01Request) -> Controller01Response:
    return Controller01Response(id=value.id, value=value.value)