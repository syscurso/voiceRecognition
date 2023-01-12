# Install SpeechRecognition with pip install SpeechRecognition
# Install pyaudio with pip install pyaudio


import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

with mic as source:

    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language = 'ES')

print(f'Has dicho: {text}')
