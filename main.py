from app.emotion_detector import detect_emotion
from app.emotion_mapper import map_emotion_to_style
from app.speech_generator import generate_speech


def main():

    print("\nEMPATHY ENGINE\n")

    text = input("Enter text:\n")

    emotion, confidence = detect_emotion(text)

    print("\nDetected Emotion:", emotion)
    print("Confidence:", round(confidence, 2))

    style = map_emotion_to_style(emotion, confidence)

    audio_file = generate_speech(text, style)

    print("\nSpeech generated:", audio_file)


if __name__ == "__main__":
    main()