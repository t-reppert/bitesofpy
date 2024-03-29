from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll export authentication further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings


app = FastAPI()
food_log: Dict[int, FoodEntry] = {}


@app.post("/", status_code=201, response_model=FoodEntry)
async def create_food_entry(food_entry: FoodEntry):
    food_log[food_entry.id] = food_entry
    return food_entry


@app.get("/{user_id}", response_model=List[FoodEntry])
async def get_foods_for_user(user_id: int):
    user_foods = [v for k, v in food_log.items() if v.user.id == user_id]
    return user_foods


@app.put("/{entry_id}", response_model=FoodEntry)
async def update_food_entry(entry_id: int, food_entry: FoodEntry):
    if entry_id not in food_log:
        raise HTTPException(status_code=404, detail="Food entry not found")
    food_log[entry_id] = food_entry
    return food_entry


@app.delete("/{entry_id}")
async def delete_food_entry(entry_id: int):
    print(food_log)
    if entry_id not in food_log:
        raise HTTPException(status_code=404, detail="Food entry not found")
    del food_log[entry_id]
    return {"ok": True}