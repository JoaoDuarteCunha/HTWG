from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/{item_id}")
async def get_test(item_id: str):
    print("Cookies:", item_id)
