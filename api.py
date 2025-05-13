from fastapi import FastAPI

app = FastAPI()

messages = []

@app.get("/")
async def root():
    message = messages.pop(0)
    return message

@app.post("/send/{message}")
async def create_item(message: str):
    messages.append(message)
    return message
