import joblib
import pandas as pd

TITLES = [
    "Product Manager",
    "Software Engineer",
    "Software Engineering Manager",
    "Data Scientist",
    "Solution Architect",
    "Technical Program Manager",
    "Human Resources",
    "Product Designer",
    "Marketing",
    "Business Analyst",
    "Hardware Engineer",
    "Sales",
    "Recruiter",
    "Mechanical Engineer",
    "Management Consultant",
]

COUNTRIES = [
    "USA",
    "United Kingdom",
    "Ireland",
    "India",
    "Belarus",
    "Canada",
    "Russia",
    "Netherlands",
    "Switzerland",
    "Singapore",
    "Germany",
    "Japan",
    "Sweden",
    "Australia",
    "United States",
    "Israel",
    "Poland",
    "China",
    "Austria",
    "Luxembourg",
    "Czech Republic",
    "France",
    "Pakistan",
    "New Zealand",
    "Denmark",
    "Hong Kong (SAR)",
    "South Africa",
    "Spain",
    "United Arab Emirates",
    "Hungary",
    "Brazil",
    "Bulgaria",
    "Philippines",
    "Indonesia",
    "Puerto Rico",
    "Taiwan",
    "Romania",
    "Mexico",
    "Costa Rica",
    "Marshall Islands",
    "Vietnam",
    "Panama",
    "Argentina",
    "Norway",
    "Moldova",
    "Estonia",
    "Kenya",
    "Turkey",
    "Italy",
    "Lithuania",
    "Nigeria",
    "Korea",
    "Ukraine",
    "Jordan",
    "Thailand",
    "Colombia",
    "Serbia",
    "Portugal",
    "Guatemala",
    "Yugoslavia",
    "Uruguay",
    "Slovakia",
    "Bangladesh",
    "Finland",
    "Chile",
    "Malaysia",
    "Latvia",
    "Saudi Arabia",
    "Peru",
    "Netherlands Antilles",
    "Belgium",
    "Burma",
    "Qatar",
    "Ghana",
    "Kazakhstan",
    "Uzbekistan",
    "Armenia",
    "Morocco",
    "Iraq",
    "Trinidad and Tobago",
    "Egypt",
]

EDUCATION_LEVELS = [
    "Bachelor",
    "Doctorate",
    "Master",
    "Both Master&Doctorate"
]

GENDERS = [
    "Male",
    "Female",
    "Other"
]

ERROR = 20704 # dollars
INFLATION = 23.97 # percentage

# Load the trained model
loaded_model = joblib.load('gradient_boost_model.joblib')

def calculate_salary(title_idx, experience, gender_idx, country_idx, education_idx):
    title = TITLES[int(title_idx)]
    gender = GENDERS[int(gender_idx)]
    country = COUNTRIES[int(country_idx)]
    education = EDUCATION_LEVELS[int(education_idx)]
    
    # Prepare data for prediction
    new_data = pd.DataFrame({
        'title': [title],
        'Education': [education],
        'gender': [gender],
        'Country': [country],
        'yearsofexperience': [experience]
    })

    # Make prediction
    prediction = loaded_model.predict(new_data)
    predicted_salary = prediction[0]

    min_predicted = predicted_salary - ERROR
    max_predicted = predicted_salary + ERROR

    min_predicted_inflated = min_predicted * ((100 + INFLATION) / 100)
    max_predicted_inflated = max_predicted * ((100 + INFLATION) / 100)

    min_predicted_int = int(min_predicted_inflated)
    max_predicted_int = int(max_predicted_inflated)

    return [min_predicted_int, max_predicted_int]
