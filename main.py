from fastapi import FastAPI

app = FastAPI()


@app.get("/test-connection")
async def root():
    return {"message": "Hello World"}
