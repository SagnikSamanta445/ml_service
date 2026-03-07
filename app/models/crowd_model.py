import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "crowd_model.pkl")

model = joblib.load(MODEL_PATH)

def crowd_score(features):

    X = [[
        features.hour_of_day,
        features.day_of_week,
        features.num_pois_100m,
        features.num_transit_stops_200m,
        {"residential":0,"mixed":1,"commercial":2}[features.area_type]
    ]]

    return float(model.predict(X)[0])
