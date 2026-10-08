# AI USAGE: I did not use generative AI for this project.

from flask import Flask, render_template
from datetime import datetime
from flask import Flask, abort, render_template

FAVORITES = [
    {"id": 1, "title": "Fantastic Mr.Fox", "why": "The colors and charming characters."},
    {"id": 2, "title": "Star Wars Episode III", "why": "The deep lore, campiness, and fight scenes."},
    {"id": 3, "title": "Swades", "why": "The international expsoure and interesting themes."}
]

MY_GAMES = [
    {"id": 1, "title": "Final Fantasy X", "releasedate": "dec 7, 2001"},
    {"id": 2, "title": "Stardew Valley", "releasedate": "feb 26, 2016"},
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

# Pages
def index():
    return render_template(
        "index.html", 
        name="Isaac Keninger",
        hobby="Playing Guitar",
        hours_per_week=4,
        fun_fact="I have 5 Tattoos",
        hour=datetime.now().hour,
        show_counter=False,
        favorites=FAVORITES,
        )

def games():
    return render_template("games.html",
                            my_games=MY_GAMES,
                            )

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/games")(games)

def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
