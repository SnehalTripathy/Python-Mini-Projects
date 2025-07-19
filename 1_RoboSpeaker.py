import pyttsx3

engine = pyttsx3.init()

print("Welcome to RoboSpeaker!")
print("Type 'exit' to quit the program.")
engine.say("Hello, I am RoboSpeaker. I can speak whatever you type.")
engine.runAndWait()
while True:
    text = input("Enter what you want to speak: ")
    if text.lower() == 'exit':
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    engine.say(text)
    engine.runAndWait()
    
