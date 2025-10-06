# 🎤 Real-Time Voice to Text with Vosk

A beautiful, real-time speech recognition web application powered by Vosk AI and Flask. Convert your speech to text instantly with a modern, responsive UI.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)

## ✨ Features

- 🎙️ **Real-time transcription** - See your words appear as you speak
- 🌐 **Offline processing** - No internet required, all processing is local
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 📱 **Responsive design** - Works on desktop and mobile devices
- 🔒 **Privacy-focused** - All speech processing happens on your machine
- ⚡ **WebSocket-powered** - Instant feedback with minimal latency
- 🐳 **Docker support** - Easy deployment with containerization

## 🚀 Quick Start

### Prerequisites

- Docker installed on your machine
- A microphone
- A modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/vosk-voice-to-text.git
   cd vosk-voice-to-text
   ```

2. **Download the Vosk model**
   
   Choose a model from [Vosk Models](https://alphacephei.com/vosk/models):
   
   For English (Small - 40MB, faster):
   ```bash
   wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
   unzip vosk-model-small-en-us-0.15.zip
   mv vosk-model-small-en-us-0.15 model
   ```
   
   For English (Large - 1.8GB, more accurate):
   ```bash
   wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
   unzip vosk-model-en-us-0.22.zip
   mv vosk-model-en-us-0.22 model
   ```

3. **Build the Docker image**
   ```bash
   docker build -t vosk-voice-to-text .
   ```

4. **Run the container**
   ```bash
   docker run -p 5000:5000 vosk-voice-to-text
   ```

5. **Open in your browser**
   ```
   http://localhost:5000
   ```

## 🛠️ Alternative: Running Without Docker

If you prefer to run without Docker:

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Vosk model** (see step 2 above)

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in your browser**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
vosk-voice-to-text/
├── app.py                  # Flask application with WebSocket support
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .gitignore             # Git ignore rules
├── model/                 # Vosk speech recognition model (not in repo)
│   └── (model files)
└── templates/
    └── index.html         # Web interface
```

## 🎯 How to Use

1. **Click "Start Listening"** - Grant microphone permissions if prompted
2. **Speak naturally** - You'll see partial text (in gray/italic) as you speak
3. **Pause briefly** - Final text appears in black after each phrase
4. **Click "Stop Listening"** - Stop the recording when done
5. **Use "Clear Text"** - Reset the transcription area

## 🌍 Supported Languages

Vosk supports many languages! Download different models from the [Vosk Models page](https://alphacephei.com/vosk/models):

- 🇺🇸 English
- 🇪🇸 Spanish
- 🇫🇷 French
- 🇩🇪 German
- 🇷🇺 Russian
- 🇨🇳 Chinese
- 🇮🇳 Hindi
- And many more!

To use a different language, just download the corresponding model and replace the `model` folder.

## ⚙️ Configuration

### Change Port

Edit the `docker run` command:
```bash
docker run -p 8080:5000 vosk-voice-to-text
```

Then access at `http://localhost:8080`

### Use Different Model

Replace the `model` folder with any Vosk model, then rebuild:
```bash
docker build -t vosk-voice-to-text .
```

## 🐛 Troubleshooting

### Microphone not working
- Ensure your browser has microphone permissions
- Check if another application is using the microphone
- Try using HTTPS or localhost (some browsers require secure context)

### No transcription appearing
- Check Docker logs: `docker logs <container-id>`
- Verify the model folder exists and contains model files
- Ensure you're speaking clearly and at normal volume

### Port already in use
```bash
# Use a different port
docker run -p 5001:5000 vosk-voice-to-text
```

### Model not found error
Make sure the `model` folder is in the project root directory before building the Docker image.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vosk](https://alphacephei.com/vosk/) - Offline speech recognition toolkit
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/) - WebSocket support

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/vosk-voice-to-text](https://github.com/yourusername/vosk-voice-to-text)

---

⭐ If you find this project useful, please consider giving it a star!