from flask import Flask, jsonify, request
from src.analyzer import most_demanded_skills, top_hiring_companies, skill_correlation_matrix

app = Flask(__name__)

@app.route("/skills/top", methods=["GET"])
def top_skills():
    n = request.args.get("n", 10, type=int)
    return jsonify(most_demanded_skills(n))

@app.route("/companies/top", methods=["GET"])
def top_companies():
    return jsonify(top_hiring_companies())

@app.route("/skills/correlation", methods=["GET"])
def skill_correlation():
    return jsonify(skill_correlation_matrix())