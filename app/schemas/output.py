from pydantic import BaseModel

class SegmentScore(BaseModel):
    segment_id: str
    safety_score: float
    safety_label: str
    confidence: float
