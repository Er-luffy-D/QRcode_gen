import qrcode
from intro import speak
speak.Speak("welcome")
c=input("ENTER YOUR WEBSITE===>\n")
img=qrcode.make(c)
img.show()
# print()
# print(qrcode.run_example("www.hi"))