def lighting_score(features):

    lights = features.num_streetlights
    complaints = features.recent_light_complaints_30d

    score = lights / (lights + complaints + 1)

    if features.hour_of_day > 22 or features.hour_of_day < 6:
        score *= 0.7

    return min(score,1)