from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI()


@app.get("/health")
async def health(settings: Settings = Depends(get_settings)):
    return {
        "status": "All good",
        "environment": settings.environment,
        "testing": settings.testing,
    }
