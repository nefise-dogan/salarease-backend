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
    title = args.get("title", default="", type=str)
    experience = args.get("experience", default=0, type=int)
    gender = args.get("gender", default="other", type=str)
    country = args.get("country", default="", type=str)
    education = args.get("education", default="", type=str)
    range = calculate_salary(title, experience, gender, country, education)
    return range
