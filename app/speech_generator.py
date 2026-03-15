import edge_tts
import asyncio
from datetime import datetime
import os


async def generate_voice(text, style, output_file):

    voice = choose_voice(style["emotion"])

    rate_value = int((style['speed'] - 1) * 100)
    rate_value = max(min(rate_value, 40), -40)

    if rate_value >= 0:
        rate = f"+{rate_value}%"
    else:
        rate = f"{rate_value}%"

    # Pitch modulation based on emotion
    pitch_map = {
        "joy": "+15Hz",
        "sadness": "-10Hz",
        "anger": "+10Hz",
        "surprise": "+20Hz",
        "fear": "+5Hz",
        "love": "+8Hz",
        "neutral": "+0Hz"
    }

    pitch = pitch_map.get(style["emotion"], "+0Hz")

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch
    )

    await communicate.save(output_file)


def generate_speech(text, style):

    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"outputs/speech_{timestamp}.mp3"

    try:
        asyncio.run(generate_voice(text, style, output_file))
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_voice(text, style, output_file))
        loop.close()

    return output_file

def choose_voice(emotion):

    voices = {
        "joy": "en-US-JennyNeural",
        "sadness": "en-GB-SoniaNeural",
        "anger": "en-US-GuyNeural",
        "surprise": "en-US-AriaNeural",
        "love": "en-US-JennyNeural",
        "fear": "en-US-DavisNeural",
        "neutral": "en-US-DavisNeural"
    }

    return voices.get(emotion, "en-US-GuyNeural")