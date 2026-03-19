# 🤖 Jarvis AI – Voice Controlled Personal Assistant

Jarvis AI is a Python-based voice assistant inspired by Iron Man.
It can perform system tasks, answer questions using AI, and interact with users using voice commands.

---

## 🚀 Features

* 🎤 Wake Word Detection ("Jarvis")
* 🗣️ Voice Recognition (Speech-to-Text)
* 🔊 Text-to-Speech Response
* 🤖 AI Integration (OpenAI API)
* 💻 System Automation (open apps, shutdown, screenshot)
* 📊 System Monitoring (battery, CPU, internet)
* 🧠 Smart Command Handling
* ⚡ Auto Start Support
* 🔐 Secure API Key Handling (Environment Variables)

---

## 🧰 Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* pvporcupine
* OpenAI API
* psutil
* pyaudio

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Setup (IMPORTANT)

### Step 1: Open Command Prompt

```text
Win + R → cmd
```

---

### Step 2: Set API Keys

```bash
setx OPENAI_API_KEY "your_openai_key"
setx PORCUPINE_KEY "your_porcupine_key"
```

---

### Step 3: Restart Terminal / VS Code

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

Say:

```text
"Jarvis"
```

Then give commands like:

* Open YouTube
* What is the time
* Shutdown system
* Take screenshot
* What is Python

---

## 📁 Project Structure

```
Jarvis/
│── main.py
│── memory.json
│── requirements.txt
│── run_jarvis.bat
│── jarvis_ui.py (optional)
```

---

## ⚡ Auto Start Setup

1. Create a `.bat` file:

```bat
cd C:\path\to\Jarvis
python main.py
```

2. Add it to:

```
Win + R → shell:startup
```

---

## 🧠 Future Improvements

* Memory System (store user data)
* GUI Dashboard (Iron Man UI)
* Offline AI Model
* Smart Context Understanding
* Mobile Integration

---

## 👨‍💻 Author

Kaushal Singh Ahirwar – B.Tech CSE Student

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
