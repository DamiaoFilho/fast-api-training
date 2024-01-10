from fastapi import FastAPI
from accounts.routers import accounts_router

app = FastAPI()
app.include_router(accounts_router.router)



sells = {
    1: {"item": "lata", "price":4, "qtd": 5},
    2: {"item": "cup", "price":10, "qtd": 10}
}


@app.get("/")
def home():
    return {"sells": len(sells)}


@app.get("/sell/{id}")
def sell(id: int):
    return sells[id]