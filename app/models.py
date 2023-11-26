#models.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    players = relationship("Player", back_populates="team")
    games_home = relationship("Game", foreign_keys="[Game.team_id_home]", back_populates="team_home")
    games_away = relationship("Game", foreign_keys="[Game.team_id_away]", back_populates="team_away")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    team_id_home = Column(Integer, ForeignKey("teams.id"))
    team_id_away = Column(Integer, ForeignKey("teams.id"))
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    team_home = relationship("Team", foreign_keys=[team_id_home], back_populates="games_home")
    team_away = relationship("Team", foreign_keys=[team_id_away], back_populates="games_away")
    