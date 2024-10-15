import os
import vosk
import sys
import wave
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import json
import subprocess

model_path = r"C:\Users\thoma\Documents\GitHub\Thomas_Lucas_Projects\Audio_to_text\vosk-model-en-us-0.22-lgraph"

os.environ["PATH"] = "C:/Users/thoma/Desktop/Code/ffmpeg-master-latest-win64-gpl/bin;" + os.environ["PATH"]

input_file = "C:/Users/thoma/Documents/GitHub/Thomas_Lucas_Projects/Audio_to_text/Audio_Files/Legacy Ln.mp3"
output_file = "C:/Users/thoma/Documents/GitHub/Thomas_Lucas_Projects/Audio_to_text/Audio_Files/new.wav"
mp4input = "C:/Users/thoma/Desktop/Fall 2024/CSE-310/VS code Github setup.mp4"
wavmp4output = "C:/Users/thoma/Documents/GitHub/Thomas_Lucas_Projects/Audio_to_text/Audio_Files/video.wav"

def Convert_mp4_to_wav(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, output_file]
    try:
        subprocess.run(command, check = True)
        print(f'Converted {input_file} to {output_file}')
        return output_file
    except subprocess.CalledProcessError as e:
        print(e)
        return None


model = Model(model_path)

# if not os.path.exists(model_path):
#     print("Model not found. Please download the model and unpack it")
#     sys.exit(1)

# try:
#     audio = AudioSegment.from_mp3(input_file)
#     audio.export(output_file, format = "wav")

#     print(f'Converted {input_file} to {output_file}')
# except Exception as e:
#     print(f'An error occured: {e}')

def Transcribe_Audio(file_path):
    wf = wave.open(file_path, "rb")
    recognizer = KaldiRecognizer(model, wf.getframerate())

    transcript = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            transcript += json.loads(result).get("text", "") + " "
        else:
            partial_result = recognizer.PartialResult()
            print(partial_result)

    final_result = recognizer.FinalResult()
    transcript += json.loads(final_result).get("text", "")

    wf.close()
    return transcript

#mp4_file = Convert_mp4_to_wav(mp4input, wavmp4output)
transcript = Transcribe_Audio(output_file)

print("Transcript:")
print(transcript)