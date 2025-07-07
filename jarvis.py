import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

listener = sr.Recognizer()

def get_command_from_audio(file_path):
    try:
        with sr.AudioFile(file_path) as source:
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            print("✅ Recognized command:", command)
            return command.lower()
    except Exception as e:
        print("❌ Speech recognition failed:", e)
        return ""


def handle_command(command):
    engine = pyttsx3.init()

    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        return f"Playing {song}"

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return f"Current time is {time}"

    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 1)
        return info

    elif 'joke' in command:
        return pyjokes.get_joke()

    elif 'weather' in command:
        return "Weather feature not supported via file input yet."

    elif 'stop' in command:
        return "Goodbye."

    else:
        return "Sorry, I didn't catch that."
