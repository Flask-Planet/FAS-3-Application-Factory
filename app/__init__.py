from flask import Flask
from app.extensions import db


def setup_routes(app: Flask) -> None:
    from app.routes.index import index_routes
    from app.routes.more import more_routes

    index_routes(app)
    more_routes(app)


def setup_models(app: Flask) -> None:
    from app.models import Example

    db.init_app(app)


def setup_blueprints(app: Flask) -> None:
    from app.blueprint import example_blueprint

    app.register_blueprint(example_blueprint)


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.DevelopmentConfig")
    # Pulls config from app/config.py

    setup_models(app)
    setup_blueprints(app)
    setup_routes(app)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
