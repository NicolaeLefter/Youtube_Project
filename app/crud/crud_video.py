from sqlalchemy.orm import Session
from models.video import Video
from schemas import VideoCreate, VideoUpdate


def create_video(db: Session, video: VideoCreate):
    db_video = Video(title=video.title, url=video.url)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


def get_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Video).offset(skip).limit(limit).all()
