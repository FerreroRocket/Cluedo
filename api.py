import flask
import database_interface
from database_interface import Round, Session, select, engine
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/round/<id>", methods=["GET"])
def get_round(id):
    session = Session(engine)
    round = session.query(Round).get(id)
    return jsonify(round.to_dict())

@app.route("/round", methods=["POST"])
def add_round():
    session = Session(engine)
    data = request.get_json()
    new_round = Round(data)
    session.add(new_round)
    session.commit()
    return jsonify(new_round.to_dict()), 201 

# Run the app with: python filename.py
if __name__ == "__main__":
    app.run(debug=True)
