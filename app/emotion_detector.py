from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=3
)


def detect_emotion(text):

    results = classifier(text)[0]

    # sort by confidence
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    primary = results[0]
    emotion = primary["label"]
    confidence = primary["score"]

    # heuristic correction
    if emotion == "surprise":
        for r in results:
            if r["label"] == "joy":
                emotion = "joy"
                confidence = r["score"]
                break

    return emotion, confidence