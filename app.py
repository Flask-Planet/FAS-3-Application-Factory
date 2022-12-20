from flask import Flask
from flask import render_template

app = Flask(__name__)
"""
Flask will look for the folders called "templates" and "static" in the root folder of the project automatically.

You can change the name of the folders Flask looks for by doing:
app = Flask(__name__, template_folder="other_templates", static_folder="other_static")
"""


# Index
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


if __name__ == "__main__":
    app.run()
