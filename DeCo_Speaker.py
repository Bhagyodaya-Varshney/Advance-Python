from win32com.client import Dispatch
print("Welcome To DeCo Speaker")
while True:
        x=input("Enter:")
        speak = Dispatch(("SAPI.SpVoice"))
        if(x=="bye" or x=="BYE" or x=="Bye"):
            speak.Speak("Thanks For Using")
            break
        speak.Speak(x)