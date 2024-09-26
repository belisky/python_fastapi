from fastapi import FastAPI
from typing import List
from models import User
from uuid import uuid4

app= FastAPI()


# db: List[User] = [
#     User(
#         id=uuid4(),
#          first_name="Nobel"
#          last_name="Fiawornu"
#          gender=Gender.male,
         



#     )

# ]
@app.get('/')
async def root():
    return {"message": "Hello Nobel"}