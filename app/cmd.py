from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Team, Player, Game

def main():
    print("Bem-vindo ao cmd.py interativo!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Listar Times")
        print("2. Listar Jogos")
        print("3. Listar Jogadores")
        print("4. Sair")

        escolha = input("Opção: ")

        if escolha == "1":
            listar_times()
        elif escolha == "2":
            listar_jogos()     
        elif escolha == "3":
            listar_jogadores()                    
        elif escolha == "4":
            print("Saindo do cmd.py. Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_times():
    db = SessionLocal()
    teams = db.query(Team).all()
    db.close()

    print("\Times:")
    for team in teams:
        print(f"ID: {team.id}, Nome: {team.name}")

def listar_jogos():
    db = SessionLocal()
    games = db.query(Game).all()

    print("\Jogos:")
    for game in games:
        team_home = db.query(Team).filter(Team.id == game.team_id_home).first()
        team_away = db.query(Team).filter(Team.id == game.team_id_away).first()

        print(f"ID: {game.id}, Nome: {team_away.name} x {team_home.name}, Data: {game.date}, Local: {game.location}")
    db.close()

def listar_jogadores():
    db = SessionLocal()
    players = db.query(Player).all()

    print("\Jogadores:")
    for player in players:
        team = db.query(Team).filter(Team.id == player.team_id).first()
        print(f"ID: {player.id}, Nome: {player.name}, Time: {team.name}")
    db.close()    

if __name__ == "__main__":
    main()