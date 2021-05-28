# Tier 1: Speech Recognition using Google Speech Recognition API
import speech_recognition as sr
import pyttsx3
import pyautogui

def sendCommandToTier2(txt):
    pyautogui.click(1440, 540)
    pyautogui.typewrite(txt)
    pyautogui.typewrite(["enter"])

# Loop infinitely for user to speak
while(1):	
    print("new loop")
    # Exception handling to handle exceptions at the runtime
    try:
        # Initialize the recognizer
        r = sr.Recognizer()
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            #r.adjust_for_ambient_noise(source2, duration=0.2)

            #listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            userMsg = MyText.split()

            for i in range(len(userMsg)):
                if userMsg[i]=="zero":
                    userMsg[i] = "0"
                elif userMsg[i]=="one":
                    userMsg[i] = "1"
                elif userMsg[i]=="two":
                    userMsg[i] = "2"
                elif userMsg[i]=="three":
                    userMsg[i] = "3"
                elif userMsg[i]=="four":
                    userMsg[i] = "4"
                elif userMsg[i]=="five":
                    userMsg[i] = "5"
                elif userMsg[i]=="six":
                    userMsg[i] = "6"
                elif userMsg[i]=="seven":
                    userMsg[i] = "7"
                elif userMsg[i]=="eight":
                    userMsg[i] = "8"
                elif userMsg[i]=="nine":
                    userMsg[i] = "9"
                elif userMsg[i]=="ten":
                    userMsg[i] = "10"
                elif userMsg[i]=="eleven":
                    userMsg[i] = "11"

            MyText = ' '.join(userMsg)

            sendCommandToTier2(MyText)
            print("Did you say "+MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")