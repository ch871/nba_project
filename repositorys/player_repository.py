from models.player_model import Player
from repositorys.create_and_delete_tables_repo import get_db_connection
from typing import List


def create_player(player: Player, season: str) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        f"""INSERT INTO {season} (
        name,
        team,
        position,
        points,
        games,
        shooting_2,
        shooting_3,
        minutes,
        at_ratio,
        ppg_ratio
         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
        (
            player.name,
            player.team,
            player.position,
            player.points,
            player.games,
            player.shooting_2,
            player.shooting_3,
            player.minutes,
            player.at_ratio,
            player.ppg_ratio
        )
    )
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id


def find_all_players(season: str) -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {season}")
    result = cursor.fetchall()
    players = [Player(**player) for player in result]
    connection.commit()
    cursor.close()
    connection.close()
    return players


def update_player(player: Player, season: str) -> Player:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
    UPDATE {season} SET 
        name = %s,
        team = %s,
        position = %s,
        points = %s,
        games = %s,
        shooting_2 = %s,
        shooting_3 = %s,
        minutes = %s,
        at_ratio = %s,
        ppg_ratio = %s
        WHERE id = %s RETURNING *
    """,
       (
           player.name,
           player.team,
           player.position,
           player.points,
           player.games,
           player.shooting_2,
           player.shooting_3,
           player.minutes,
           player.at_ratio,
           player.ppg_ratio,
           player.id
       )
    )
    updated_player = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return updated_player


def delete_player(player_id: int):
    seasons = ["2024", "2023", "2022"]
    connection = get_db_connection()
    cursor = connection.cursor()
    for season in seasons:
        cursor.execute(f'DELETE FROM {season} WHERE id = %s ', player_id)
    connection.commit()
    cursor.close()
    connection.close()
    return
