from datetime import time
import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt","whatsapp":"whatsapp"}

def openappweb(query):
    speak("opening, please wait")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("mini","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def execute_command(query):
    speak("opening whatsapp")
    if "whatsapp" in query:
        # Press Windows + S to open the search bar
        pyautogui.hotkey("win", "s")
        sleep(0.5)
        # Type 'WhatsApp' in the search bar
        pyautogui.write("WhatsApp")
        sleep(0.5)
        # Press Enter to open WhatsApp
        pyautogui.press("enter")
    
def voicetype(query):
    speak("Now you can type by telling")
    if "want to type" in query:
        pyautogui.hotkey("win","h")

def closeapp(query):
    speak("Closing ")
    if "close whatsapp" in query:
        pyautogui.hotkey("alt","f4")
        sleep(0.5)
        pyautogui.hotkey("alt","f4")
        speak("whatsapp closed")

def closeappweb(query):
    speak("Closing ")
    if "one tab" in query or "1 tab" in query or "this tab" in query or "this tab also" in query:
        pyautogui.hotkey("ctrl","w")
        speak("tab closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("2 tabs closed")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("3 tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All 4 tabs closed")
        
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")


