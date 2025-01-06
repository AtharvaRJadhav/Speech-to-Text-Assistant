import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

FILENAME_FROM_MIC = "RECORDING.WAV"
VOICE_TEXT_FILENAME = "VOICE_AS_TEXT.txt"

# Initialize the recognizer
r = sr.Recognizer()

def recognize_from_file(filename):
    try:
        with sr.AudioFile(filename) as source:
            print(f"Processing file: {filename}")
            audio_data = r.record(source)  # Load audio data into memory
            text = r.recognize_google(audio_data)  # Convert speech to text
            return text
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
        return ""

def recognize_from_microphone(file_to_write):
    try:
        SAMPLE_RATE = 44100
        duration = 5  # seconds
        print("Recording audio...")
        audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate=SAMPLE_RATE, channels=1, dtype='int32')
        sd.wait()  # Wait for recording to complete
        print("Audio recording complete. Playing back...")
        sd.play(audio_recording, SAMPLE_RATE)  # Play back the recording
        sd.wait()  # Wait for playback to complete
        wav.write(file_to_write, SAMPLE_RATE, audio_recording)  # Save as WAV file
        print(f"Recording saved as '{file_to_write}'.")
    except Exception as e:
        print(f"An error occurred during recording: {e}")

def save_text_to_file(text, filename):
    try:
        with open(filename, 'w') as f:
            f.write(text)
        print(f"Text saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the text: {e}")

if __name__ == "__main__":
    try:
        recognize_from_microphone(FILENAME_FROM_MIC)  # Record and save audio
        text_from_voice = recognize_from_file(FILENAME_FROM_MIC)  # Transcribe audio
        if text_from_voice:  # Check if transcription was successful
            save_text_to_file(text_from_voice, VOICE_TEXT_FILENAME)  # Save transcription
        else:
            print("No text to save.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
