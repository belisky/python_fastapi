from typing import List, Optional
from src.commons.postgres import database
from src.trainers.trainers_schema import Trainer

async def get_trainer_by_email(email: str) -> Optional[Trainer]:
    query = "SELECT name, email FROM trainers WHERE email = $1"
    async with database.pool.acquire() as connection:
        row = await connection.fetchrow(query, email)
        if row is not None:
            trainer = trainer(name=row["first_name"]+row["last_name"], email=row["email"]) 
            return trainer
        return None

async def get_all_trainers(limit: int, offset: int) -> List[Trainer]:
    query = "SELECT name, email FROM trainers LIMIT $1 OFFSET $2"
    async with database.pool.acquire() as connection:
        rows = await connection.fetch(query, limit, offset)
        trainers = [Trainer(name=record["first_name"]+record["last_name"], email=record["email"]) for record in rows]
        return trainers
    
async def insert_trainer(trainer: Trainer):
    query = "INSERT INTO trainers (first_name,last_name, email) VALUES ($1, $2)"
    async with database.pool.acquire() as connection:
        await connection.execute(query, trainer.first_name, trainer.last_name,trainer.email)

async def bulk_insert_trainers(trainers: List[Trainer]):
    query = "INSERT INTO trainers (first_name,last_name, email) VALUES ($1, $2)"
    user_tuples = [(trainer.first_name,trainer.last_name, trainer.email) for trainer in trainers]
    async with database.pool.acquire() as connection:
        await connection.executemany(query, user_tuples)