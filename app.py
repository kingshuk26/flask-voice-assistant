from flask import Flask, render_template, request, jsonify
from jarvis import get_command_from_audio, handle_command
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("jarvis.html")

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio file received'}), 400

    audio = request.files['audio_data']
    filepath = "temp.wav"
    audio.save(filepath)

    command = get_command_from_audio(filepath)
    response = handle_command(command)

    os.remove(filepath)
    return jsonify({'command': command, 'response': response})

if __name__ == '__main__':
    app.run(debug=True)
