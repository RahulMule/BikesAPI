from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.gameschema import CreateGame, Gameschema,ReviewSchema,ReviewCreate
from ..database.db import get_db
from ..models.gamesmodel import Game,GameStat,Review

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

@gamesrouter.post("/{id}/review", response_model=ReviewSchema,status_code=status.HTTP_201_CREATED)
def addreview(id : int,review: ReviewCreate, db : Session = Depends(get_db)):
    review = Review(score=review.score,comment=review.comment,gameid=id)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

@gamesrouter.get("/{gameid}/review", response_model=list[ReviewSchema], status_code=status.HTTP_200_OK)
def getgamereview(gameid : int, db: Session=Depends(get_db)):
    reviews = db.query(Review).filter(Review.gameid==gameid).all()
    if not reviews:
        raise HTTPException(status_code=404, detail="Reviews are not available")
    return reviews