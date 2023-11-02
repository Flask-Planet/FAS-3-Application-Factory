from flask import Flask
from flask import render_template


def more_routes(app: Flask):
    @app.route('/more')
    def more():
        return render_template("more.html")

    @app.route('/even-more')
    def even_more():
        return render_template("more.html")
