import uvicorn
from fastapi import FastAPI
from app.routers import controller01

# Create an instance of FastAPI
app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"Informations": "This is our first example."}

app.include_router(controller01.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)