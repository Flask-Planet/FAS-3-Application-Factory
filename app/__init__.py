from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_views(app: Flask) -> None:
    from app.views.index import index_views

    index_views(app)


def setup_models(app: Flask) -> None:
    from app.models import Example

    db.init_app(app)


def setup_blueprints(app: Flask) -> None:
    from app.blueprint import example_blueprint

    app.register_blueprint(example_blueprint)


def create_app():
    from app.models import Example

    app = Flask(
        __name__,
        static_host="",
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    setup_models(app)
    setup_blueprints(app)
    setup_views(app)

    with app.app_context():
        db.create_all()

    return app
