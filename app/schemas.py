from pydantic import BaseModel


class LanguageBase(BaseModel):
    name: str
    code: str


class Language(LanguageBase):
    id: int

    class Config:
        orm_mode = True


class Message(BaseModel):
    status: str
    text: str
