from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from vosk import Model, KaldiRecognizer
import json
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Load Vosk model
MODEL_PATH = "model"
model = Model(MODEL_PATH)

# Store recognizers for each client
recognizers = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Create a recognizer for this client
    recognizers[request.sid] = KaldiRecognizer(model, 16000)
    recognizers[request.sid].SetWords(True)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    # Clean up recognizer
    if request.sid in recognizers:
        del recognizers[request.sid]

@socketio.on('audio_data')
def handle_audio(data):
    try:
        # Get the recognizer for this client
        rec = recognizers.get(request.sid)
        if not rec:
            return
        
        # Decode base64 audio data
        audio_data = base64.b64decode(data)
        
        # Process audio
        if rec.AcceptWaveform(audio_data):
            result = json.loads(rec.Result())
            if result.get('text'):
                emit('transcription', {
                    'text': result['text'],
                    'final': True
                })
        else:
            # Partial result
            partial = json.loads(rec.PartialResult())
            if partial.get('partial'):
                emit('transcription', {
                    'text': partial['partial'],
                    'final': False
                })
    except Exception as e:
        print(f"Error processing audio: {e}")
        emit('error', {'message': str(e)})

@socketio.on('audio_end')
def handle_audio_end():
    try:
        rec = recognizers.get(request.sid)
        if rec:
            final = json.loads(rec.FinalResult())
            if final.get('text'):
                emit('transcription', {
                    'text': final['text'],
                    'final': True
                })
    except Exception as e:
        print(f"Error in final result: {e}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
