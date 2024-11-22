# Description: Pydantic data models dictate what is passed between frontend and backend.

from typing import Optional

from pydantic import BaseModel


class Players(BaseModel):
    id: Optional[str] = ""
    public_key: str
    note_id: str
    game: str
    game_id: str
    amount: int
    boss: str

class Games(BaseModel):
    id: str
    game: str
    wallet: str
    enabled: bool

class Nsec(BaseModel):
    boss: str
    nsec: str