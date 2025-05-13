from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    message: str
    
app = FastAPI()

messages = []

class Message

@app.get("/")
async def root():
    message = messages.pop(0)
    return message

@app.post("/send/")
async def create_item(message: Message):
    print(message)
    messages.append(message)
    return message
