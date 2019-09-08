# import pyttsx3 as tts
from gtts import gTTS


def main():
    tts = gTTS(text='صباح الخير', lang='ar')
    tts.save("good.mp3")


if __name__ == '__main__':
    main()
