from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..dependencies import get_db

router = APIRouter()


async def create_video(video: schemas.VideoCreate, db: Session)
