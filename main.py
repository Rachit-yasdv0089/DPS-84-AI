import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import time
import phonenumbers
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
import pyautogui
import psutil

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hi, I am DPS-84 AI. How may I help you today?")
    print("Hi, I am DPS-84 AI. How may I help you today?")

    speak("You can speak the commands when it shows Listening...  and wait when it shows Recognizing...")
    speak("To know more about the commands please speak, What are the commands.")
    
def takecommand():
    # It uses the mic as the input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # Adjust this value based on your environment
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return "None"
    
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('raorachitsingh@gmail.com', '')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()  

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    
    # logic for executing tasts 
        if 'what are the commands' in query:
            print("The commands are:: Open youtube, Open google, What is the time, What is the weather, Do basic calculations, Generate a password, let's play rock paper scissors, start a countdown and search anything on wikipedia")
            commands = speak("The commands are:: Open youtube, Open google, What is the time, What is the weather, Do basic calculations, Generate a password, let's play rock paper scissors, start a countdown and search anything on wikipedia")
            
        
        
        
        
        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        

        elif 'open youtube' in query:
            speak("opening Youtube...")
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            speak("opening Google...")
            webbrowser.open("Google.com")

        # elif 'play music' in query:
        #     music_dir = 'C:\\Users\\raora\\OneDrive\\Desktop\\music for Stem'
        #     songs = os.listdir(music_dir)
        #     print (songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M%S")
            speak(f"The time is {strTime}")

        # elif 'send email' in query:
        #     try:
        #         speak('what should i say?')
        #         content = takecommand()
        #         to = "raorachitsingh@gmail.com"
        #         sendEmail(to, content)
        #         speak('Email has been sent!')
        #     except Exception as e:
        #         print (e)
        #         speak('sorry I was not able to send your email.')



        elif 'what is the weather' in query:
            speak('the weather today is')
            webbrowser.open("https://www.accuweather.com/en/in/gurgaon/188408/daily-weather-forecast/188408")

        elif 'do basic calculations' in query:
            speak("Enter the values below")
            x = input("Enter the first value here:: ")
            
            z = input("Enter the second value here:: ")
            
            speak("Type the function you want to perform below.")
            c = input("which function do you want me to do (as a symbol):: ")
            
            
            if c == "+":
                sum = int(x) + int(z)
                print("The answer is:: ",sum)
            
            if c == "*":
                product = int(x) * int(z)
                print("The answer is:: ", product)
            
            if c == '/':
                division = int(x) / int(z)
                print ("The answer is:: ", division)
            
            if c == '-':
                minus = int(x) - int(z)
                print ("The answer is:: ", minus)

        elif 'generate a password' in query:
            pd="abcd4572stvxwyz#@!$&"
            num=int(input("enter password length:"))
            a=random.sample(pd,num)
            c="".join(a)
            print("random password is :",c)

        elif "let's play rock paper scissors" in query:
            options = ("rock", "paper", "scissors")
            running = True

            while running:

                player = None
                computer = random.choice(options)

                while player not in options:
                    player = input("Enter a choice (rock, paper, scissors): ")

                print(f"Player: {player}")
                print(f"Computer: {computer}")

                if player == computer:
                    print("It's a tie!")
                elif player == "rock" and computer == "scissors":
                    print("You win!")
                elif player == "paper" and computer == "rock":
                    print("You win!")
                elif player == "scissors" and computer == "paper":
                    print("You win!")
                else:
                    print("You lose!")

                if not input("Play again? (y/n): ").lower() == "y":
                    running = False

            print("Thanks for playing!")
            
        elif 'start a countdown' in query:
            seconds = int(input("write the countdown in seconds:: "))
            for i in range (seconds, 0, -1):
            
                timeleft = print(str(i) + 'seconds left')
                time.sleep(1)
                
            print ('time is up')

        # elif 'location' in query:
        #     in_number = phonenumbers.parse(number, "in")
        #     number_location = print(geocoder.description_for_number(in_number, "en"))       
        #     service_number = phonenumbers.parse(number)   
            
        #     key = 'ce982b24be174e6f98379c2c5ea7f46b'
        #     geocoder = OpenCageGeocode(key)

        #     nigga = str(number_location)
        #     results = geocoder.geocode(nigga)

        #     lat = results[0]["geometry"]['lat']
        #     lng = results[0]['geometry']['lng']
        #     print(lat, lng)

        #     map_location = folium.Map(location = [lat, lng], zoom_start=91)
        #     folium.Marker([lat, lng], popup=number_location).add_to(map_location)
        #     map_location.save("mylocation.html")


