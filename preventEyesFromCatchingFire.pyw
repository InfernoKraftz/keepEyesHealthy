import win32com.client as wc
import time
speaker = wc.Dispatch('SAPI.SpVoice')
while True:
    time.sleep(895)
    speaker.Speak("Time to look away from your screen to keep your eyes healthy. Look away at a faraway object other than a device for 10 seconds!")
    print("Time to look away from your screen to keep your eyes healthy. Look away at a faraway object other than a device for 10 seconds!")