from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.gameschema import CreateGame, Gameschema
from ..database.db import get_db
from ..models.gamesmodel import Game,GameStat

gamesrouter = APIRouter(
    prefix="/games",
    tags=['Games']
)

@gamesrouter.get("/", response_model= list[Gameschema],status_code=status.HTTP_200_OK)
def geallgames(db: Session = Depends(get_db)):
    allgames = db.query(Game).all()
    if not allgames:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return allgames

@gamesrouter.get("/{id}",response_model=Gameschema,status_code=status.HTTP_200_OK)
def getgamebyid(id:int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id==id).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return game

@gamesrouter.post("/",response_model=Gameschema, status_code=status.HTTP_201_CREATED)
def addgame(game:CreateGame, db: Session = Depends(get_db)):
    
    gamestat = GameStat(downloads=game.gamestat.downloads,rating=game.gamestat.rating,livegamers=game.gamestat.livegamers)
    game = Game(name=game.name,genre=game.genre,price=game.price,gamestat=gamestat)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

@gamesrouter.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletegame(id: int, db : Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id==id).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="game not found")
    db.delete(game)
    db.commit()
    return status.HTTP_204_NO_CONTENT