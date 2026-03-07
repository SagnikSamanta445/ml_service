def aggregate_scores(crowd, shop, lighting, haven):

    safety = (
        0.30*crowd +
        0.20*shop +
        0.30*lighting +
        0.20*haven
    )

    return min(max(safety,0),1)