from ..database.db import base,engine
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Game(base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True,nullable=False)
    name= Column(String,nullable=False)
    genre = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    gamestat =relationship(
        "GameStat",
        back_populates="game",
        uselist=False
        )
    review = relationship("Review",back_populates="game",cascade="all, delete")

class GameStat(base):
    __tablename__ = "gamestats"
    id = Column(Integer,primary_key=True)
    downloads = Column(Integer,nullable=False)
    rating = Column(Integer,nullable=False)
    livegamers = Column(Integer,nullable=False)
    gameid = Column(Integer, ForeignKey("games.id"), unique=True)
    game = relationship("Game", back_populates="gamestat")


class Review(base):
    __tablename__ = "Reviews"
    id = Column(Integer, primary_key=True)
    score = Column(Integer,nullable=False)
    comment = Column(String,nullable=False)
    gameid = Column(Integer,ForeignKey("games.id"))
    game = relationship("Game",back_populates="review")

    
base.metadata.create_all(engine)


