# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_team_api, create_player_api, create_game_api, delete_game_api, get_players_by_team_api, delete_player_api, read_teams_api, get_team_details_api, delete_team_api, read_games_api,read_players_api, update_game_api, update_player_api, update_team_api
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/teams/")
def create_team(name: str, db: Session = Depends(get_db)):
    return create_team_api(db, name)

@app.get("/teams/")
def read_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return read_teams_api(db, skip, limit)

@app.get("/teams/{team_id}/details")
def get_team_details(team_id: int, db: Session = Depends(get_db)):
    return get_team_details_api(db, team_id)

@app.put("/teams/{team_id}/update")
def update_team(team_id: int, name: str, db: Session = Depends(get_db)):
    return update_team_api(db, team_id, name)

@app.post("/players/")
def create_player(name: str, team_id: int, db: Session = Depends(get_db)):
    return create_player_api(db, name, team_id)

@app.get("/players/")
def read_players(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    return read_players_api(db, skip, limit)

@app.put("/players/{player_id}")
def update_player(player_id: int, name: str, team_id: int, db: Session = Depends(get_db)):
    return update_player_api(db, player_id, name, team_id)

@app.get("/teams/{team_id}/players")
def get_players_by_team(team_id: int, db: Session = Depends(get_db)):
    return get_players_by_team_api(db, team_id)

@app.post("/games/")
def create_game(team_id_home: int, team_id_away: int, date: str, location: str, db: Session = Depends(get_db)):
    return create_game_api(db, team_id_home, team_id_away, date, location)

@app.get("/games/")
def read_games(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return read_games_api(db, skip, limit)

@app.put("/games/{game_id}")
def update_game(game_id: int, team_id_home: int, team_id_away: int, date: str, location: str, db: Session = Depends(get_db)):
    return update_game_api(db, game_id, team_id_home, team_id_away, date, location)

@app.delete("/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    return delete_team_api(db, team_id)

@app.delete("/teams/{team_id}/players/{player_id}")
def delete_player(team_id: int, player_id: int, db: Session = Depends(get_db)):
    return delete_player_api(db, team_id, player_id)

@app.delete("/games/{game_id}")
def delete_game(game_id: int, db: Session = Depends(get_db)):
    return delete_game_api(db, game_id)
