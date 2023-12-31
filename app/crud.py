# crud.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Team, Player, Game

def create_team_api(db: Session, name: str):
    team = Team(name=name)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def update_team_api(db: Session, team_id: int, name: str):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Time não encontrado")

    team.name = name

    db.commit()
    db.refresh(team)

    return team

def update_player_api(db: Session, player_id: int, name: str, team_id: int):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")

    player.name = name
    player.team_id = team_id

    db.commit()
    db.refresh(player)

    return player

def create_player_api(db: Session, name: str, team_id: int):
    player = Player(name=name, team_id=team_id)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def create_game_api(db: Session, team_id_home: int, team_id_away: int, date: str, location: str):
    teams = db.query(Team).filter(Team.id.in_([team_id_home, team_id_away])).all()
    if team_id_home == team_id_away:
        raise HTTPException(status_code=400, detail="Time não pode jogar contra si mesmo!") 
    if len(teams) != 2:
        raise HTTPException(status_code=404, detail="Um ou ambos os times não foram encontrados")  

    game = Game(date=date, location=location, team_home=teams[0], team_away=teams[1])

    db.add(game)
    db.commit()
    db.refresh(game)
    return game

def read_games_api(db: Session, skip: int = 0, limit: int = 20):
    games = db.query(Game).offset(skip).limit(limit).all()
    game_list = [{"id": game.id, "date": game.date, "location": game.location, "team_home": db.query(Team).filter(Team.id == game.team_id_home).first().name, "team_away": db.query(Team).filter(Team.id == game.team_id_away).first().name} for game in games]
    return game_list

def update_game_api(db: Session, game_id: int, team_id_home: int, team_id_away: int, date: str, location: str):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    teams = db.query(Team).filter(Team.id.in_([team_id_home, team_id_away])).all()
    if team_id_home == team_id_away:
        raise HTTPException(status_code=400, detail="Um time não pode jogar contra si mesmo!") 
    if len(teams) != 2:
        raise HTTPException(status_code=404, detail="Um ou ambos os times não foram encontrados")  

    game.team_home = teams[0]
    game.team_away = teams[1]
    game.date = date
    game.location = location

    db.commit()
    db.refresh(game)

    return game

def get_players_by_team_api(db: Session, team_id: int):
    players = db.query(Player).filter(Player.team_id == team_id).all()
    return players

def delete_player_api(db: Session, team_id: int, player_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Time não encontrado")

    player = db.query(Player).filter(Player.id == player_id, Player.team_id == team_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Jogador não encontrado no time")

    db.delete(player)
    db.commit()
    return {"message": "Jogador deletado com sucesso"}

def read_teams_api(db: Session, skip: int = 0, limit: int = 10):
    teams = db.query(Team).offset(skip).limit(limit).all()
    team_list = [{"id": team.id, "name": team.name} for team in teams]
    return team_list

def read_players_api(db: Session, skip: int = 0, limit: int = 15):
    players = db.query(Player).offset(skip).limit(limit).all()
    player_list = [{"id": player.id, "name":player.name, "team": db.query(Team).filter(Team.id == player.team_id).first().name} for player in players]

    return player_list

def get_team_details_api(db: Session, team_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    
    team_players = get_players_by_team_api(db, team_id)
    team_games_home = db.query(Game).filter(Game.team_id_home == team_id).all()
    team_games_away = db.query(Game).filter(Game.team_id_away == team_id).all()

    games_home_details = [{"game_id": game.id, "date": game.date, "location": game.location, "contra": game.team_away} for game in team_games_home]
    games_away_details = [{"game_id": game.id, "date": game.date, "location": game.location, "contra": game.team_home} for game in team_games_away]

    team_details = {
        "team_id": team.id,
        "team_name": team.name,
        "players": [{"player_id": player.id, "player_name": player.name} for player in team_players],
        "games_home": games_home_details,
        "games_away": games_away_details,
    }

    return team_details

def delete_team_api(db: Session, team_id: int):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Time não encontrado")

    db.delete(team)
    db.commit()
    return {"message": "Time deletado com sucesso"}

def delete_game_api(db: Session, game_id: int):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    db.delete(game)
    db.commit()
    return {"message": "Jogo deletado com sucesso"}
