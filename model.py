import random

def calculate_salary(title, experience, gender, country, education):
    print("Calculate salary based on these parameters:")
    print(title, experience, gender, country, education)
    start_salary = random.randint(100, 4000)
    end_salary = random.randint(100, 4000)
    min_salary = min(start_salary, end_salary) * 100
    max_salary = max(start_salary, end_salary) * 100
    return [min_salary, max_salary]
