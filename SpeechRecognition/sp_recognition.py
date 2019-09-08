import speech_recognition as sr


class SpRecognition:

    def __init__(self, audio=None):
        self.audio = audio
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def audio_recognize(self, show_all=False):
        while self.audio is None:
            self.audio = input("Enter audio path:")
        try:
            with sr.AudioFile(self.audio) as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.record(source)
            return self.r.recognize_google(audio, show_all=show_all)
        except sr.UnknownValueError():
            print("Unrecognized speech")

    def mic_recognize(self):
        try:
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)
            return self.r.recognize_google(audio)
        except sr.UnknownValueError():
            print("Unrecognized speech")

    def list_all_mic_devices(self):
        return sr.Microphone.list_microphone_names()

