from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Enterprise AI Agent Platform",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "platform": "Enterprise AI Agent Platform",
        "status": "running"
    }
