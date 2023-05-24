from app import db


class Example(db.Model):
    example_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Example {self.name}>"
