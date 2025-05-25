from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('api/data.json') as f:
    students = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = []
    for name in names:
        student = next((s for s in students if s["name"] == name), None)
        marks.append(student["marks"] if student else None)
    return jsonify({"marks": marks})
