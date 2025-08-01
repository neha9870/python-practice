import speech_recognition as sr
import pyttsx3
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hey Neha, how may I help you")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=2)


        print("recognizing...")
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))            

