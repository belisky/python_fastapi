import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.commons.postgres import database
from src.students.students_route import students_router
from src.trainers.trainers_route import trainers_router

@asynccontextmanager
async def lifespan(app: FastAPI):
  await database.connect()
  yield
  await database.disconnect()

 
app = FastAPI(lifespan=lifespan)
app.include_router(students_router)
app.include_router(trainers_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")