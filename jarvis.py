import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json

listener = sr.Recognizer()
engine = pyttsx3.init()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    return text

def weather(city):
    api_key = 'your_weather_api_key'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        return f"{x['main']['temp']}°C with {x['weather'][0]['description']}"
    else:
        return "City not found"

def get_command_from_audio(audio_path):
    try:
        with sr.AudioFile(audio_path) as source:
            audio = listener.record(source)
            command = listener.recognize_google(audio)
            return command.lower()
    except Exception as e:
        return f"Could not process audio: {str(e)}"

def handle_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        return engine_talk(f"Playing {song}")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return engine_talk(f"The current time is {time}")

    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 1)
        return engine_talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        return engine_talk(joke)

    elif 'weather' in command:
        city = command.replace('weather in', '').strip()
        return engine_talk(weather(city))

    else:
        return engine_talk("Sorry, I didn't understand that.")
