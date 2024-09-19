from flask import Flask
from repositorys.create_and_delete_tables_repo import drop_all_tables,create_players_table
from services.sid_service import sid
from services.data_service import filtered_data


app = Flask(__name__)

if __name__ == '__main__':
    drop_all_tables()
    create_players_table()
    sid(filtered_data)
    app.register_blueprint(user_bluprint, url_prefix="/api/user")

    app.run(debug=True)