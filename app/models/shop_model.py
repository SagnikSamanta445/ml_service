import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "shop_model.pkl")

model = joblib.load(MODEL_PATH)

def shop_score(features):

    X = [[
        features.hour_of_day,
        features.num_shops_100m,
        {"residential":0,"mixed":1,"commercial":2}[features.area_type]
    ]]

    return float(model.predict_proba(X)[0][1])