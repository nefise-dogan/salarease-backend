from flask import Flask, request
from flask_cors import CORS
from model import calculate_salary

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return 'This is the backend server for SalarEase'

@app.route('/calculate', methods=['GET'])
def search():
    args = request.args
    title_idx = args.get("title_idx", default="", type=str)
    experience = args.get("experience", default=0, type=int)
    gender_idx = args.get("gender_idx", default="", type=str)
    country_idx = args.get("country_idx", default="", type=str)
    education_idx = args.get("education_idx", default="", type=str)
    range = calculate_salary(title_idx, experience, gender_idx, country_idx, education_idx)
    return range
