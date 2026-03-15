def map_emotion_to_style(emotion, confidence):

    base_speed = {

        "joy": 1.05,
        "love": 1.03,
        "surprise": 1.08,

        "anger": 1.02,
        "fear": 0.95,

        "sadness": 0.90,
        "neutral": 1.0
    }

    base = base_speed.get(emotion, 1.0)

    # intensity scaling
    speed = base * (1 + confidence * 0.2)

    style = {
        "speed": speed,
        "emotion": emotion   # ← IMPORTANT
    }

    return style