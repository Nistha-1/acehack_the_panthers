import speech_recognition as sr



r = sr.Recognizer()
my_mic=sr.Microphone(device_index=1)


with my_mic as source:
    print("Talk")
    r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source)
    print("Time over, thanks")

    
    
    print(r.recognize_google(audio_text))
    