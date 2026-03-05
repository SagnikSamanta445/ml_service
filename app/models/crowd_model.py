def crowd_score(f):
    score = 0.0

    score += min(f.num_pois_100m / 10, 1.0) * 0.4
    score += min(f.num_transit_stops_200m / 5, 1.0) * 0.3

    if f.area_type == "commercial":
        score += 0.3
    elif f.area_type == "mixed":
        score += 0.15

    if f.hour_of_day >= 22:
        score *= 0.6

    return min(score, 1.0)
