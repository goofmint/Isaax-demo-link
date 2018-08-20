#!/usr/bin/env python3

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 44100, chunk_size = 512) as source:
    audio = r.listen(source)
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio, language='ja-JP'))
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
