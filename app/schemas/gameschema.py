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



class ReviewBase(BaseModel):
    score: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    gameid : int
    model_config={
        'from_attributes':True
    }

class ReviewSchema(ReviewBase):
    id : int
    gameid : int
    model_config={
        'from_attributes':True
    }

class Gameschema(GamesBase):
    id: int
    gamestat: GameStat
    model_config={
        'from_attributes':True
    }

class CreateGame(GamesBase):
    gamestat: GameStatBase