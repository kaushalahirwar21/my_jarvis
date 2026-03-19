import webbrowser
import os
import datetime
import pyttsx3
import pvporcupine
import pyaudio
import speech_recognition as sr
from openai import OpenAI
import psutil
import socket

# ================= CONFIG =================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
PORCUPINE_KEY = os.getenv("PORCUPINE_KEY")

# ================= VOICE =================
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ================= SYSTEM REPORT =================
def system_report():
    battery = psutil.sensors_battery()
    cpu = psutil.cpu_percent()

    try:
        socket.create_connection(("8.8.8.8", 53))
        internet = "connected"
    except:
        internet = "not connected"

    speak(f"Battery is {battery.percent} percent")
    speak(f"CPU usage is {cpu} percent")
    speak(f"Internet is {internet}")

# ================= AI =================
def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("AI ERROR:", e)
        return "Bhai AI abhi kaam nahi kar raha"

# ================= WAKE WORD =================
def wake_word():
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_KEY,
        keywords=["jarvis"]
    )

    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🟡 Waiting for 'Jarvis'...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = memoryview(pcm).cast('h')

            if porcupine.process(pcm) >= 0:
                print("🔥 Wake word detected!")
                speak("Ha bhai, bol kya kaam hai")
                return

    finally:
        stream.close()
        pa.terminate()
        porcupine.delete()

# ================= LISTEN =================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Bhai samajh nahi aaya")
        return ""

# ================= START =================
print("🔥 Jarvis starting...")
speak("System online bhai")
system_report()

# ================= MAIN LOOP =================
while True:
    wake_word()

    command = listen()

    if command == "":
        continue

    if "hello" in command:
        speak("Hello bhai")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time_now}")

    elif "system report" in command:
        system_report()

    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "open vscode" in command:
        speak("Opening VS Code")
        os.system("code")

    elif "screenshot" in command:
        import pyautogui
        pyautogui.screenshot("screen.png")
        speak("Screenshot taken")

    elif "stop" in command:
        speak("Goodbye bhai")
        break

    elif len(command.split()) > 2:
        speak("Thinking bhai")
        answer = ask_ai(command)
        speak(answer)

    else:
        speak("Command not recognized")

    speak("Anything else bhai?")