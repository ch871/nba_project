from flask import Blueprint, jsonify
from dataclasses import asdict
from repositorys.player_repository import find_all_players

user_bluprint = Blueprint("user", __name__)


@user_bluprint.route("/season", method=['GET'])
def get_all():
    users = list(map(asdict, find_all_players("2024")))
    return jsonify(users), 200