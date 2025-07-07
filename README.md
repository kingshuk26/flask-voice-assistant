Title of Project: Jarvis: A Web-Based Voice Assistant

Inspired by J.A.R.V.I.S. from Iron Man, this browser-based AI assistant was developed using Flask and Speech Recognition. Using a microphone button in the browser, this assistant records your voice, processes it with Python, and then does things like play music, tell the time, make jokes, and retrieve data.
Demo
![Screenshot 2025-07-07 204220](https://github.com/user-attachments/assets/a4b83834-950a-4eeb-8ab8-d5f1333d21a0)
![Screenshot 2025-07-07 204252](https://github.com/user-attachments/assets/fca98231-eecb-47b9-91a9-a7fd9caeab34)

🛠️ Tech Stack
Frontend:
HTML5, CSS3 (Bootstrap)
JavaScript (MediaRecorder API)

Backend:
Python
Flask

Libraries:
speech_recognition
pyttsx3
pywhatkit
wikipedia
pyjokes
pydub (for audio conversion)

✨ Features

🎤 Take voice input from mic via browser
🔊 Respond using text-to-speech
📺 Play YouTube videos
🕒 Tell the current time
📖 Fetch summaries from Wikipedia
😂 Tell jokes using pyjokes
🌦️ (Upcoming) Weather functionality
Simple Flask API backend
Real-time feedback displayed on the web page

📂 Folder Structure
Voice Assistant/
├── app.py               # Flask web server
├── jarvis.py            # Core assistant logic
├── templates/
│   └── jarvis.html      # Web UI
├── static/              # Optional (for CSS/JS/image files)
├── venv/                # Virtual environment (excluded from GitHub)


🔧 Setup Instructions
1. Clone the repository
   git clone https://github.com/your-username/voice-assistant-flask.git
   cd voice-assistant-flask
2. Create and activate a virtual environment
   python -m venv venv
   .\venv\Scripts\activate   # On Windows
3. Install dependencies
   pip install -r requirements.txt
   Flask
  speechrecognition
  pyttsx3
  pywhatkit
  wikipedia
  pyjokes
  pydub
4. Install FFmpeg (Required for pydub)
   Download and install from: https://ffmpeg.org/download.html
   Add ffmpeg/bin to your system PATH

▶️ Run the App
    python app.py

Open in browser:
http://127.0.0.1:5000

💡 Future Improvements
✅ Add voice output in browser using Web Speech API
✅ Add support for continuous speech
🔒 Add user authentication
🌐 Deploy to Render/Heroku/Vercel
📱 Convert to PWA for mobile use

🙋‍♂️ Author
Kingshuk https://github.com/kingshuk26
B.Tech Computer Science Undergraduate

📄 License
This project is open source and available under the MIT License.

     
  
