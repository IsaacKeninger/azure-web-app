from flask import Flask, render_template
from datetime import datetime
from flask import Flask, abort, render_template


FAVORITES = [
    {"id": 1, "title": "Fantastic Mr.Fox", "why": "The colors and charming characters."},
    {"id": 2, "title": "Star Wars Episode III", "why": "The deep lore, campiness, and fight scenes."},
    {"id": 3, "title": "Swades", "why": "The international expsoure and interesting themes."}
]

def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

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

def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorite.html", favorite=favorite)
    abort(404)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
