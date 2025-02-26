from fastapi import FastAPI

app = FastAPI()  # FastAPI 애플리케이션 객체 생성

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/ping")
async def ping():
    return {"message": "pong!"}