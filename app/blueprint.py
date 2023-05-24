from flask import Blueprint

example_blueprint = Blueprint("api", __name__, url_prefix="/example-blueprint")


@example_blueprint.get("/")
def get():
    return {"request_success": True, "message": "Hello World!"}


@example_blueprint.post("/post")
def post():
    return {"request_success": True, "message": "Hello World!"}


@example_blueprint.route("/get-or-post", methods=["GET", "POST"])
def get_or_post():
    return {"request_success": True, "message": "Hello World!"}
