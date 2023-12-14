import joblib
import pandas as pd

# Load the trained model
loaded_model = joblib.load('gradient_boost_model.joblib')

# Make predictions
new_data = pd.DataFrame({
    'title': ['Product Manager'],
    'Education': ['Both Master&Doctorate'],
    'gender': ['Female'],
    'Country': ['USA'],
    'yearsofexperience': [10.0]
})

prediction = loaded_model.predict(new_data)

print(f"Predicted base salary: {prediction}")
