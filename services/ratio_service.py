from typing import List

from models.player_model import Player


def points_per_game(tow_points: int, three_points: int, games: int) -> float:
    total_points = (tow_points * 2) + (three_points * 3)
    return total_points / games


def at_ratio(assist: int, turnovers: int) -> float:
    return assist / turnovers


def ppg_ratio(players):
    total_points = 0
    devid_to_memutza = 0
    for player in players:
        total_points += points_per_game(player["twoFg"], player["threeFg"], player["games"])
        devid_to_memutza += 1
    return total_points / devid_to_memutza
