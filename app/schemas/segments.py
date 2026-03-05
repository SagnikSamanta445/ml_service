from pydantic import BaseModel

class SegmentFeatures(BaseModel):
    segment_id: str
    hour_of_day: int
    day_of_week: int
    area_type: str

    num_pois_100m: int
    num_shops_100m: int
    num_food_shops_100m: int
    num_transit_stops_200m: int

    num_streetlights: int
    recent_light_complaints_30d: int
    days_since_last_light_complaint: int

    distance_to_police_m: float
    distance_to_petrol_pump_m: float
    distance_to_hospital_m: float

    incident_count_1yr: int
