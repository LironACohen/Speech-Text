import speech_recognition as sr
import subprocess


class SpeechToText:


    def stt(self, file_name):
        # Creating a Recognizer instance
        r = sr.Recognizer()

        # Checking if it is a OPUS file and decoding it into a WAV file if needed
        if file_name.find('opus') != -1:
            changing_format = 'opusdec ' + file_name + ' ' + 'NewWaveFile.wav'
            subprocess.run(changing_format, shell=True)
            file_name = 'NewWaveFile.wav'

        # Creating a Audio file instance
        # This class can be initialized with the path to an audio file and provides
        # a context manager interface for reading and working with the file’s contents.
        audio_wav = sr.AudioFile(file_name)

        with audio_wav as source:
            # Cleaning the audio source from beckround noise
            r.adjust_for_ambient_noise(source)

            # Using record() to Capture Data From a File
            audio = r.record(source)

            # Crating a new txt file in the relevent Path
            try:
                myText = open(r'new file name.txt', 'w')
                myText.write(r.recognize_google(audio))
                myText.close()
                return myText
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand audio"
            except sr.RequestError as e:
                return "Could not request results from Google Speech Recognition service; {0}".format(e)
