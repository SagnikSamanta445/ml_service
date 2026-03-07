from fastapi import FastAPI
from app.schemas.segments import SegmentFeatures

from app.models.crowd_model import crowd_score
from app.models.shop_model import shop_score
from app.models.lighting_model import lighting_score
from app.models.safe_haven_model import safe_haven_score
from app.models.aggregator import aggregate_scores

app = FastAPI()


@app.post("/score-segment")
def score_segment(segment: SegmentFeatures):

    c = crowd_score(segment)
    s = shop_score(segment)
    l = lighting_score(segment)
    h = safe_haven_score(segment)

    safety = aggregate_scores(c, s, l, h)

    return {
        "segment_id": segment.segment_id,
        "safety_score": safety,
        "safety_label": "SAFE" if safety > 0.7 else "CAUTION" if safety > 0.4 else "AVOID",
        "confidence": abs(safety - 0.5) * 2
    }


@app.get("/")
def root():
    return {"status": "ok"}