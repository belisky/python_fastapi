import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.commons.postgres import database


@asynccontextmanager
async def lifespan(app: FastAPI):
  await database.connect()
  yield
  await database.disconnect()

 
app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")