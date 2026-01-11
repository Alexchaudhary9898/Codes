import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime
model = Model("model")
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()
def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))
def process_query(query):
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"the current time is {now}"
    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        response = f"todays date is {today}"
    else:
        response = "im sorry. i didnt understand that"
    return response
print("voice assistant started")
print("say 'time', 'data' or exit")
speak("hello, i am ready to listen")
with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback
):
    while True:
        data = audio_queue.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                print("you said:", text)
                response = process_query(text)
                print("Assistant:", response)
                speak(response)