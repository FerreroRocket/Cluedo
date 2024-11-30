import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

engine = create_engine("postgresql://postgres:6624@localhost:5432/", echo=True)

class Base(DeclarativeBase):
    pass

class Round(Base):
    __tablename__ = "rounds"
    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))
    round_number: Mapped[Optional[int]]
    asker: Mapped[Optional[int]]
    helper: Mapped[Optional[int]]
    person: Mapped[Optional[str]]
    weapon: Mapped[Optional[str]]
    room: Mapped[Optional[str]]
    card: Mapped[Optional[str]]
    def __repr__(self) -> str:
         return f"Round(id={self.id!r})"

class Game(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True)

session = Session(engine)
rounds = select(Round)
for round in session.scalars(rounds):
    print(round)