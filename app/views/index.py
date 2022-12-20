from flask import render_template


def index_views(app):
    @app.route('/')
    def index():
        stringv = "value"
        intv = 1
        floatv = 1.1
        boolv = True
        listv = ["value1", "value2", "value3"]
        dictv = {"key1": "value1", "key2": "value2", "key3": "value3"}
        return render_template(
            "index.html",
            stringv=stringv,
            intv=intv,
            floatv=floatv,
            boolv=boolv,
            listv=listv,
            dictv=dictv
        )