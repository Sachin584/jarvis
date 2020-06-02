import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Morning")
    
    speak("I am Jarvis sir, please tell how may I help you")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        speak("i am sorry sir can you please repeat")
        print("Please say that again")
        return "None"

    return query

if __name__=="__main__":
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'stop' in query:
            break;

        if 'wikipedia' in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'google search' in query:
            speak("searching on google")
            query = query.replace("google", "")
            webbrowser.open(query)
            # speak()

        elif 'open youtube' in query:
            speak("sure sir")
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            speak("sure sir")
            webbrowser.open("stackoverflow.com")   

        elif 'open facebook' in query:
            speak("sure sir")
            webbrowser.open("facebook.com")

        elif 'open music' in query:
            music_dir = 'C:\\Users\\Sachin\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        # Talks
        elif 'how are you' in query:
            speak("i am good sir")
            speak("how are you sir")

        elif 'hello' in query:
            speak("hello sir")
            speak("how can i help you")

        elif 'your name' in query:
            speak("i am jarvis sir")

        elif 'what are you doing' in query:
            speak("i am free sir")
            speak("any command sirr")

            

        