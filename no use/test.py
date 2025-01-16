import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)  # Adjust for background noise
        print("Listening...")
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=5)
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")

        except Exception as e:
            print("Say that again")
            return "None"
        return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe  # Ensure the GreetMe module exists
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime.")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you?")

                elif "i am fine" in query:
                    speak("That's great, sir!")

                elif "how are you" in query:
                    speak("Perfect, sir!")

                elif "how r u" in query:
                    speak("Perfect, sir!")

                elif "thank you" in query:
                    speak("You're welcome, sir!")
