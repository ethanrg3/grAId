from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import random
import uvicorn

app = FastAPI()

# Mock database
users_db = {}
questions_db = {
    1: {"question": "What is 2 + 2?", "answers": ["3", "4", "5", "6", "7", "8", "9", "10", "1", "2"], "correct": 1},
    2: {"question": "What is the capital of France?", "answers": ["Berlin", "Madrid", "Paris", "Lisbon", "Rome", "Vienna", "Athens", "Dublin", "Oslo", "Stockholm"], "correct": 2},
}
user_progress = {}

class UserRegister(BaseModel):
    username: str
    grade: int
    handedness: str
    gender: str

class Answer