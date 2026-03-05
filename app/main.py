from fastapi import FastAPI
from app.schemas.segments import SegmentFeatures
from app.models.crowd_model import crowd_score

app = FastAPI()

@app.post("/score-segment")
def score_segment(segment: SegmentFeatures):
    
    c = crowd_score(segment)

    return {
      "segment_id": segment.segment_id,
      "safety_score": c,
      "safety_label": "SAFE" if c > 0.7 else "CAUTION",
      "confidence": abs(c - 0.5) * 2
    }

@app.get("/")
def root():
    return {"status": "ok"}

