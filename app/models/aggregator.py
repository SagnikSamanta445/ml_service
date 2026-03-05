def aggregate(scores, hour):
    w = {
        "crowd": 0.30,
        "shop": 0.20,
        "lighting": 0.25,
        "safe_haven": 0.15,
        "incident": 0.10
    }

    if hour >= 22:
        w["lighting"] += 0.1
        w["crowd"] += 0.1

    safety = (
        w["crowd"] * scores["crowd"]
        - w["incident"] * scores["incident"]
    )

    return max(min(safety, 1), 0)
