# Speech-to-Text Assistant

A Python-based speech-to-text application that leverages your microphone to record audio, transcribes the speech to text using Google's Speech Recognition API, and saves the results to a `.txt` file.

## Features
- **Audio Recording**: Records a 5-second audio clip from your microphone.
- **Audio Playback**: Plays back the recorded audio for verification.
- **Speech-to-Text Conversion**: Converts the audio recording into text.
- **Text Saving**: Saves the transcribed text into a `.txt` file.

---

## Requirements

- Python 3.7 or higher
- Required Python packages:
  - `speech_recognition`
  - `sounddevice`
  - `numpy`
  - `scipy`

---

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/speech-to-text-assistant.git
   cd speech-to-text-assistant
