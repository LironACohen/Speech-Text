from gtts import gTTS


class TextToSpeech:

    def tts(self, file_name):
        # define variables
        data = open(file_name, 'r').read().replace('\n', ' ')
        file = 'Output.mp3'

        # initialize tts, create mp3 and play
        tts = gTTS(data, lang = 'en', slow = False)
        tts.save(file)