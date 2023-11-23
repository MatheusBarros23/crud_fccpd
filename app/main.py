from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")

Team.players = relationship("Player", back_populates="team")

DATABASE_URL = "postgresql://user:password@db/db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.post("/teams/")
def create_team(name: str):
    db = SessionLocal()
    team = Team(name=name)
    db.add(team)
    db.commit()
    db.refresh(team)
    db.close()
    return team

@app.get("/teams/{team_id}/")
def read_team(team_id: int):
    db = SessionLocal()
    team = db.query(Team).filter(Team.id == team_id).first()
    db.close()
    return team