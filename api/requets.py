import requests


def get_pliers_from_api(season):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={season}&&pageSize=1000"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return "trivia not found"
    else:
        return f"Error {response.status_code}: {response.text}"
