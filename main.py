import speech_recognition as sr
import os
import google.generativeai as genai
import webbrowser
import openai
import pyjokes
import smtplib
import datetime
import requests
import random



chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(prompt):
    global chatStr
    print(chatStr)

    genai.configure(api_key="AIzaSyCFo9WmPMCNK0AP_Cjg0D3OvDFG3qqbzQA")
    # Set up the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 0,
      "max_output_tokens": 8192,
    }
    
    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
      },
    ]
    
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    
    convo = model.start_chat(history=[
      {
        "role": "user",
        "parts": ["write an email to boss for resignation"]
      },
      {
        "role": "model",
        "parts": ["[\n {\n  \"subject\": \"Resignation - Your Name\",\n  \"body\": \"Dear [Boss's name],\\n\\nPlease accept this email as formal notification that I am resigning from my position as [Your position] at [Company name]. My last day of employment will be [Your last day].\\n\\nThank you for the opportunity to work at [Company name] for the past [Number] years. I have enjoyed my time here and appreciate the opportunities I have been given to [List of things you've learned or experiences you've had]. I have learned a lot and grown both professionally and personally.\\n\\nI wish you and the company all the best in the future. Please let me know if there is anything I can do to help during this transition.\\n\\nSincerely,\\n[Your name]\"\n }\n]"]
      },
    ])
    chatStr += f"shiva: {prompt}\n shana: "
    convo.send_message(prompt)
    text=convo.last.text
    print(text)
    say(text)
    return text


def ai(prompt):
    genai.configure(api_key="AIzaSyCFo9WmPMCNK0AP_Cjg0D3OvDFG3qqbzQA")
    say(prompt.split('intelligence')[1:])
    # Set up the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 0,
      "max_output_tokens": 8192,
    }
    
    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
      },
    ]
    
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    
    convo = model.start_chat(history=[
      {
        "role": "user",
        "parts": ["write an email to boss for resignation"]
      },
      {
        "role": "model",
        "parts": ["[\n {\n  \"subject\": \"Resignation - Your Name\",\n  \"body\": \"Dear [Boss's name],\\n\\nPlease accept this email as formal notification that I am resigning from my position as [Your position] at [Company name]. My last day of employment will be [Your last day].\\n\\nThank you for the opportunity to work at [Company name] for the past [Number] years. I have enjoyed my time here and appreciate the opportunities I have been given to [List of things you've learned or experiences you've had]. I have learned a lot and grown both professionally and personally.\\n\\nI wish you and the company all the best in the future. Please let me know if there is anything I can do to help during this transition.\\n\\nSincerely,\\n[Your name]\"\n }\n]"]
      },
    ])
    
    convo.send_message(prompt)
    text=convo.last.text
    print(text)

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from shana"

if __name__ == '__main__':
    print('Welcome to shana the famous A.I')
    say("hey shiva , i am shana  ")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/shivanandbhatia/Downloads/milange.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
        elif "open spotify".lower() in query.lower():
            os.system(f"open /System/Applications/Spotify.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "shana Quit".lower() in query.lower():
            exit()
        elif "exit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
        elif 'email to shiva' in query:
            try:
                say("What should I say?")
                content = takeCommand()
                to = "Receiver email address"   
                sendEmail(to, content)
                say("Email has been sent !")
            except Exception as e:
                print(e)
                say("I am not able to send this email")

        elif 'joke' in query:
            say(pyjokes.get_joke())
        else:
            print("Chatting...")
            chat(query)




        # say(query)