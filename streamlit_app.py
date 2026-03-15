import streamlit as st
from app.emotion_detector import detect_emotion
from app.emotion_mapper import map_emotion_to_style
from app.speech_generator import generate_speech

st.set_page_config(page_title="Empathy Engine", layout="centered")

st.title("Empathy Engine")
st.subheader("AI Emotion Detection + Emotional Speech Generator")

text = st.text_area("Enter your text")

if st.button("Generate Speech"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        emotion, confidence = detect_emotion(text)

        style = map_emotion_to_style(emotion, confidence)

        audio_file = generate_speech(text, style)

        st.success("Speech Generated!")

        st.write(f"**Emotion:** {emotion}")
        st.write(f"**Confidence:** {confidence:.2f}")

        st.audio(audio_file)