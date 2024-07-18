from flask import Flask, render_template_string, request, jsonify
import random
import datetime
import wikipedia
import webbrowser
import time

app = Flask(__name__)

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DPS-84 AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            margin-bottom: 20px;
            font-family: 'Arial Black', sans-serif;
            color: #333;
        }
        input {
            padding: 10px;
            width: 300px;
            margin-right: 10px;
        }
        button {
            padding: 10px;
            margin-right: 10px;
        }
        p {
            margin-top: 20px;
            font-weight: bold;
        }
        .recognizing {
            color: red;
        }
        .logo {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="{{ url_for('static', filename='dps_logo.png') }}" alt="DPS Logo" class="logo" width="150">
        <h1>DPS-84 AI</h1>
        <input type="text" id="command-input" placeholder="Enter your command">
        <button onclick="sendCommand()">Send</button>
        <button onclick="startListening()">Speak</button>
        <p id="response"></p>
        <p id="status"></p>
    </div>
    <script>
        function sendCommand() {
            const command = document.getElementById('command-input').value;
            fetch('/api/command', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ command: command }),
            })
            .then(response => response.json())
            .then(data => {
                const responseText = data.response;
                document.getElementById('response').innerText = responseText;
                speak(responseText);
            });
        }

        function startListening() {
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = 'en-US';
            recognition.start();

            recognition.onstart = function() {
                document.getElementById('status').innerText = 'Listening...';
                document.getElementById('status').classList.add('recognizing');
            }

            recognition.onend = function() {
                document.getElementById('status').innerText = '';
                document.getElementById('status').classList.remove('recognizing');
            }

            recognition.onresult = function(event) {
                const command = event.results[0][0].transcript;
                document.getElementById('command-input').value = command;
                sendCommand();
            };

            recognition.onerror = function(event) {
                console.error(event.error);
                alert('Error occurred in recognition: ' + event.error);
            };
        }

        function speak(text) {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.onend = function() {
                console.log('Speech has finished');
            }
            utterance.onerror = function(event) {
                console.error('Error occurred in speech synthesis: ' + event.error);
            }
            speechSynthesis.speak(utterance);
        }
    </script>
</body>
</html>
"""

# Routes
@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/api/command', methods=['POST'])
def handle_command():
    data = request.json
    query = data.get('command', '').lower()

    if 'wikipedia' in query:
        response = "Searching Wikipedia..."
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        response += f" According to Wikipedia: {results}"
    elif 'open youtube' in query:
        response = "Opening Youtube..."
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in query:
        response = "Opening Google..."
        webbrowser.open("https://www.google.com")
    elif 'what is the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The time is {strTime}"
    elif 'do basic calculations' in query:
        response = "Enter the values in the frontend"
    elif 'generate a password' in query:
        pd = "abcd4572stvxwyz#@!$&"
        num = random.randint(8, 12)
        a = random.sample(pd, num)
        c = "".join(a)
        response = f"Random password is: {c}"
    elif "let's play rock paper scissors" in query:
        response = "Let's play! Enter your choice in the frontend"
    elif 'start a countdown' in query:
        try:
            countdown_time = int(query.split('countdown ')[1])
            response = f"Countdown started for {countdown_time} seconds."
            time.sleep(countdown_time)
            response += " Countdown finished!"
        except Exception as e:
            response = "Error starting countdown."

    else:
        response = "Command not recognized"

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
