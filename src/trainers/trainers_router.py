from typing import Optional, List
from fastapi import APIRouter
from src.trainers import trainers_model
from src.trainers.trainers_schema import Trainer

trainers_router = APIRouter(prefix="/trainers")

@trainers_router.get("/")
async def get_all_trainers(limit=10, offset=0):
    return await trainers_model.get_all_trainers(limit, offset)

@trainers_router.get("/{email}")
async def get_trainer_by_email(email: str):
    return await trainers_model.get_trainer_by_email(email)

# @trainers_router.post("/")
# async def insert_trainer(trainer: Trainer):
#     return await trainers_model.insert_trainer(trainer)

# @trainers_router.post("/bulk")
# async def bulk_insert_trainers(trainers: List[Trainer]):
#     return await trainers_model.bulk_insert_trainers(trainers)