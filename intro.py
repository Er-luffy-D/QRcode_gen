#just import this program , then run===> syntax---->
#  speak.Speak("what you want to pronounce")

import win32com.client as wn
speak=wn.Dispatch("SAPI.SpVoice")