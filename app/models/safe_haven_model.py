import math

def safe_haven_score(features):

    d = min(
        features.distance_to_police_m,
        features.distance_to_petrol_pump_m,
        features.distance_to_hospital_m
    )

    tau = 300  # decay constant

    score = math.exp(-d/tau)

    return score