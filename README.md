# Empathy Engine

### AI Emotion Detection and Emotional Speech Generation

Empathy Engine is an AI-powered system that detects emotions in text and generates emotionally expressive speech.
The system analyzes the emotional tone of a sentence using a transformer-based model and converts the text into speech with voice modulation that reflects the detected emotion.

This project demonstrates how natural language understanding and speech synthesis can be combined to create more human-like conversational AI systems.

---

## Features

* Emotion detection using transformer-based NLP models
* Emotion confidence scoring
* Emotion-to-speech style mapping
* Dynamic speech modulation (rate and pitch)
* Emotion-specific neural voices
* Emotional speech generation using neural text-to-speech
* Interactive web interface built with Streamlit

---

## Supported Emotions

The system currently detects and generates speech for the following emotional categories:

* Joy
* Sadness
* Anger
* Fear
* Surprise
* Love
* Neutral

Each emotion produces a different speaking style using voice selection and modulation.

---

## System Architecture

```
User Text Input
        │
        ▼
Emotion Detection (Transformer Model)
        │
        ▼
Emotion + Confidence Score
        │
        ▼
Emotion Style Mapping
        │
        ▼
Voice Selection + Speech Modulation
        │
        ▼
Neural Text-to-Speech Generation
        │
        ▼
Emotionally Expressive Audio Output
```

---

## Project Structure

```
empathy-engine
│
├── app
│   ├── emotion_detector.py
│   ├── emotion_mapper.py
│   └── speech_generator.py
│
├── streamlit_app.py
├── main.py
├── requirements.txt
└── README.md
```

### File Description

| File                | Purpose                            |
| ------------------- | ---------------------------------- |
| emotion_detector.py | Detects emotion from input text    |
| emotion_mapper.py   | Maps emotion to speech parameters  |
| speech_generator.py | Generates speech using neural TTS  |
| streamlit_app.py    | Web interface for the application  |
| main.py             | Command-line version of the system |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/empathy-engine.git
cd empathy-engine
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Streamlit Web Interface

Run the web application:

```bash
streamlit run streamlit_app.py
```

Then open your browser and navigate to:

```
http://localhost:8501
```

You can enter any sentence and hear the emotionally expressive speech output.

---

### Command Line Version

You can also run the command-line version:

```bash
python main.py
```

---

## Example

Input text:

```
I am extremely happy today!
```

Detected emotion:

```
Emotion: joy
Confidence: 0.98
```

Generated output:

* Cheerful voice
* Faster speech rate
* Higher pitch modulation

---

## Technologies Used

* Python
* Streamlit
* Transformers
* PyTorch
* Edge Neural Text-to-Speech

---

## Applications

This technology can be used in many real-world systems:

* Conversational AI assistants
* Emotion-aware chatbots
* Voice interfaces
* Accessibility tools
* Interactive storytelling
* Mental health support tools

---

## Future Improvements

Possible future enhancements include:

* Real-time speech emotion detection
* Multilingual emotional speech synthesis
* Emotion intensity control
* Dialogue-based conversational systems
* Deployment as a cloud API

---

## Author

Vijay Narasimha Gowd

---

## License

This project is open source and available for educational and research purposes.
