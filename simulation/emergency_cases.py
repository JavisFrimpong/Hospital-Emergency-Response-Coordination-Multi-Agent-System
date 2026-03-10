# Mock emergency cases to be used by the environment

import random

def get_random_patient():
    patients = [
        "Patient_Alpha", "Patient_Bravo", "Patient_Charlie",
        "Patient_Delta", "Patient_Echo", "Patient_Foxtrot",
        "Patient_Golf", "Patient_Hotel", "Patient_India"
    ]
    return random.choice(patients)

def get_random_severity():
    severity_levels = ["Low", "Medium", "High", "Critical"]
    return random.choice(severity_levels)
