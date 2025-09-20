import win32com.client

# Initialize SAPI voice
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Speak something

speaker.Rate=4
speaker.Volume=100

list=["jagannath","Rahul","Sohan","Guru","Ranjan","Alok","Biswa","Rinku"]

for i in range(len(list)):
    speaker.speak(f"Hello {list[i]}")

# voices=speaker.GetVoices()

# for i,voice in enumerate(voices):
#     print(i,voice.GetDescription())

# speaker.Voice=voices.Item(1)
# speaker.speak("Now I am using another voice")