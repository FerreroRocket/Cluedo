import flask
import database_interface
from database_interface import Round, Session, select, engine
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/round/<id>", methods=["GET"])
def home(id):
    session = Session(engine)
    round = session.query(Round).get(id)
    return jsonify(round.to_dict())

# Run the app with: python filename.py
if __name__ == "__main__":
    app.run(debug=True)
