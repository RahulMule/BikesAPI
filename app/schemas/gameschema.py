from pydantic import BaseModel



class GameStatBase(BaseModel):
    downloads: int
    rating: int
    livegamers: int

class GameStat(GameStatBase):
    id: int
    model_config={
        'from_attributes':True
    }

class GamesBase(BaseModel):
    name: str
    genre: str
    price: int

class Gameschema(GamesBase):
    id: int
    gamestat: GameStat
    model_config={
        'from_attributes':True
    }

class CreateGame(GamesBase):
    gamestat: GameStatBase