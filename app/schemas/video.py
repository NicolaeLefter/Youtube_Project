from pydantic import BaseModel


class VideoBase(BaseModel):
    title: str
    url: str


class VideoCreate(VideoBase):
    pass


class VideoUpdate(VideoBase):
    pass


class Video(VideoBase):
    id: int
    is_valid: bool

    class Config:
        orm_mode = True
