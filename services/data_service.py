from api.requets import get_pliers_from_api
from toolz import pipe, map, partial

seasons = ["2024", "2023", "2022"]
data = [get_pliers_from_api(season) for season in seasons]


def filter_data(data_list):
    season_2024 = pipe(
        data_list[0],
        partial(map, lambda dl: {"playerName": dl["playerName"],
                                 "minutesPg": dl["minutesPg"],
                                 "team": dl["team"],
                                 "position": dl["position"],
                                 "games": dl["games"],
                                 "threeFg": dl["threeFg"],
                                 "twoFg": dl["twoFg"],
                                 "assists": dl["assists"],
                                 "turnovers": dl["turnovers"]}
                ),
        list
    )
    season_2023 = pipe(
        data_list[1],
        partial(map, lambda dl: {"playerName": dl["playerName"],
                                 "position": dl["position"],
                                 "games": dl["games"],
                                 "threeFg": dl["threeFg"],
                                 "twoFg": dl["twoFg"],
                                 "assists": dl["assists"],
                                 "turnovers": dl["turnovers"]}
                ),
        list
    )
    season_2022 = pipe(
        data_list[2],
        partial(map, lambda dl: {"playerName": dl["playerName"],
                                 "position": dl["position"],
                                 "games": dl["games"],
                                 "threeFg": dl["threeFg"],
                                 "twoFg": dl["twoFg"],
                                 "assists": dl["assists"],
                                 "turnovers": dl["turnovers"]}
                ),
        list
    )
    return {"season_2024": season_2024, "season_2023": season_2023, "season_2022": season_2022, }

filtered_data = filter_data(data)

