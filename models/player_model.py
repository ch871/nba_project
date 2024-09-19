from dataclasses import dataclass


@dataclass
class Player:
    name: str
    team: str
    position: str
    points: int
    games: int
    shooting_2: int
    shooting_3: int
    minutes: float
    at_ratio: float
    ppg_ratio: float
    id: int = None
