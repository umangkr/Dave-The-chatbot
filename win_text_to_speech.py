import win32com.client as wincl
def talk(sp):
    speak=wincl.Dispatch("SAPI.SpVoice")
    speak.speak(sp)
