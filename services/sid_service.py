from models.player_model import Player
from services.ratio_service import at_ratio,points_per_game,ppg_ratio
from repositorys.create_and_delete_tables_repo import create_players_table, drop_all_tables
from repositorys.player_repository import create_player


def sid(data):
    drop_all_tables()
    create_players_table()
    for key, season in data.items():
        for play in season:
            player = Player(
                name=play["playerName"],
                minutes=play["minutesPg"],
                position=play["position"],
                team=play["team"],
                games=play["games"],
                shooting_2=play["twoFg"],
                shooting_3=play["threeFg"],
                points=(play["twoFg"]* 2) + (play["threeFg"] * 3),
                at_ratio=at_ratio(play["assists"],play["turnovers"]),
                ppg_ratio=points_per_game(play["twoFg"], play["threeFg"], play["games"]) / ppg_ratio(data))
            create_player(player, key)



