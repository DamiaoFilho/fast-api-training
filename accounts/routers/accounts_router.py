from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


class AccountGet(BaseModel):
    id: int
    name: str
    price: int

class AccountPost(BaseModel):
    name: str
    price: int



router = APIRouter(prefix="/accounts")


@router.get("/get", response_model=List[AccountGet])
def account_get():
    return [
        AccountGet(
            id=1,
            name="test",
            price=10,
        )
    ]


@router.post("/post", response_model=AccountPost, status_code=201)
def account_get(account: AccountPost):
    return AccountPost(
        name=account.name,
        price=account.price,
    )
    