from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///opportunities.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

TEXT_FIELDS = ("title", "description", "area", "faculty", "department",
               "skills", "deadline", "status")


class Opportunity(db.Model):
    __tablename__ = "research_opportunities"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    area = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(250), nullable=False)
    positions = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False)

    def as_json(self):
        data = {name: getattr(self, name) for name in TEXT_FIELDS}
        data["id"] = self.id
        data["positions"] = self.positions
        return data

    def apply(self, values):
        for name, value in values.items():
            setattr(self, name, value)


with app.app_context():
    db.create_all()


def read_payload():
    """Validate the JSON body. Returns (values, error_message)."""
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return None, "Request body must be JSON"

    values = {}
    for name in TEXT_FIELDS:
        raw = str(body.get(name, "")).strip()
        if not raw:
            return None, f"'{name}' is required"
        values[name] = raw

    try:
        values["positions"] = int(body.get("positions"))
    except (TypeError, ValueError):
        return None, "'positions' must be a whole number"
    if values["positions"] < 0:
        return None, "'positions' cannot be negative"

    return values, None


def not_found():
    return jsonify({"error": "Opportunity not found"}), 404


# ---------- pages ----------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- API ----------
@app.get("/api/researchtitles")
def list_opportunities():
    rows = Opportunity.query.order_by(Opportunity.id.desc()).all()
    return jsonify([row.as_json() for row in rows])


@app.get("/api/researchtitles/<int:item_id>")
def get_opportunity(item_id):
    row = db.session.get(Opportunity, item_id)
    return jsonify(row.as_json()) if row else not_found()


@app.post("/api/researchtitles")
def add_opportunity():
    values, error = read_payload()
    if error:
        return jsonify({"error": error}), 400
    row = Opportunity(**values)
    db.session.add(row)
    db.session.commit()
    return jsonify(row.as_json()), 201


@app.put("/api/researchtitles/<int:item_id>")
def edit_opportunity(item_id):
    row = db.session.get(Opportunity, item_id)
    if not row:
        return not_found()
    values, error = read_payload()
    if error:
        return jsonify({"error": error}), 400
    row.apply(values)
    db.session.commit()
    return jsonify(row.as_json())


@app.delete("/api/researchtitles/<int:item_id>")
def remove_opportunity(item_id):
    row = db.session.get(Opportunity, item_id)
    if not row:
        return not_found()
    db.session.delete(row)
    db.session.commit()
    return jsonify({"message": "Opportunity deleted"})


if __name__ == "__main__":
    app.run(debug=True)