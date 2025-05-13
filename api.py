from fastapi import FastAPI

app = FastAPI()

messages = []

@app.get("/")
async def root():
    message = messages.pop(0)
    return message

@app.post("/send/")
async def create_item(message: str):
    print(message)
    messages.append(message)
    return message
