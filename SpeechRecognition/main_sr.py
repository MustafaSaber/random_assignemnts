from SpeechRecognition.sp_recognition import SpRecognition


def main():
    sp = SpRecognition()
    # print(sp.mic_recognize())
    print(sp.audio_recognize())


if __name__ == '__main__':
    main()

