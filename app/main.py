from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    players = relationship("Player", back_populates="team")
    games = relationship("Game", back_populates="team")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)

    team = relationship("Team", back_populates="games")

engine = create_engine("postgresql://user:password@db/db")
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



@app.post("/players/")
def create_player(name: str, team_id: int):
    db = SessionLocal()
    player = Player(name=name, team_id=team_id)
    db.add(player)
    db.commit()
    db.refresh(player)
    db.close()
    return player

@app.post("/games/")
def create_game(team_id: int, date: str, location: str):
    db = SessionLocal()
    game = Game(team_id=team_id, date=date, location=location)
    db.add(game)
    db.commit()
    db.refresh(game)
    db.close()
    return game


@app.get("/teams/{team_id}/players")
def get_players_by_team(team_id: int):
    db = SessionLocal()
    players = db.query(Player).filter(Player.team_id == team_id).all()
    db.close()
    return {"players": players}

@app.delete("/teams/{team_id}/players/{player_id}")
def delete_player(team_id: int, player_id: int):
    db = SessionLocal()
    
    # Verificar se o time existe
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        db.close()
        raise HTTPException(status_code=404, detail="Time não encontrado")

    # Verificar se o jogador pertence ao time
    player = db.query(Player).filter(Player.id == player_id, Player.team_id == team_id).first()
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Jogador não encontrado no time")

    # Deletar o jogador
    db.delete(player)
    db.commit()
    db.close()

    return {"message": "Jogador deletado com sucesso"}

@app.get("/teams/")
def read_teams(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    teams = db.query(Team).offset(skip).limit(limit).all()
    db.close()
    team_list = [{"id": team.id, "name": team.name} for team in teams]
    return team_list