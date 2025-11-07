from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File, Form
import os
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="CIKS Backend", description="CIKS Backend API")
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "..", "media")
OUTFITS_DIR = os.path.join(MEDIA_ROOT, "outfits")
os.makedirs(OUTFITS_DIR, exist_ok=True)

app.mount("/media", StaticFiles(directory=MEDIA_ROOT), name="media")

OUTFITS: list[dict] = []



@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ciks-backend"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Outfit(BaseModel):
    id: str
    date: str
    occasion: Optional[str] = None
    notes: Optional[str] = None
    photo_url: str
    