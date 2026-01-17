import speech_recognition as sr 
import pyttsx3
from datetime import datetime
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rare', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer
    with sr.Microphone() as source:
        print("?? speak now")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f" you said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print(" could not understand")
        except sr.RequestError as e:
            print(f" API error: {e}")
    return""
def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True
def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
main()