from models.player_model import Player
from repositorys.create_and_delete_tables_repo import get_db_connection
from typing import List


def create_player(player: Player, season: int) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        f"""INSERT INTO nba (
        name,
        team,
        position,
        points,
        games,
        shooting_2,
        shooting_3,
        minutes,
        at_ratio,
        ppg_ratio,
        season
         ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
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
            season
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
    cursor.execute(f"SELECT * FROM nba WHERE season = %s",(season,))
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
    UPDATE nba SET 
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
        WHERE id = %s AND season = %s"RETURNING *
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
           player.id,
           season
       )
    )
    updated_player = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return updated_player


def delete_player(player_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM nba WHERE id = %s ', player_id)
    connection.commit()
    cursor.close()
    connection.close()
    return
