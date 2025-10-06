FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install flask flask-socketio vosk python-socketio[client] eventlet

# Copy application files
COPY app.py .
COPY templates templates/

# Copy model (make sure you have the model folder in your project directory)
COPY model model/

EXPOSE 5000

# Use eventlet for WebSocket support
CMD ["python", "app.py"]
