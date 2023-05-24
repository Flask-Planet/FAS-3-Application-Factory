from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# this import needs to be relative (.views.ind...) as views is not a package
from app.views.index import index_views

db = SQLAlchemy()


def create_app():
    from app.models import Example

    app = Flask(
        __name__,
        static_host="",
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    index_views(app)

    return app
