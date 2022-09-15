import speech_recognition as s_r
import vlc
import os

import asyncio
import time

from gtts import gTTS

def fire_and_forget(f):
  def wrapped(*args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
  return wrapped

@fire_and_forget
def play_lullaby():
  audio = "audios/lullabies/forest-lullaby-110624.mp3"
  # p = vlc.MediaPlayer(audio)
  # p.play()
  os.system("mpg123 " + audio)

def speak_transcript(transcript):
  # Generate the audio using the gTTS engine. We are passing the message and the language
  audio = gTTS(text=transcript, lang='en')
  # Save the audio in MP3 format
  audio.save("message.mp3")
  # Play the MP3 file
  os.system("mpg123 message.mp3")

r = s_r.Recognizer()
my_mic = s_r.Microphone()
while (1):
  with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone

    # with open("audio_file.wav", "wb") as file:
    #   file.write(audio.get_wav_data())
  try: 
    # transcript = r.recognize_google(audio, language="el-GR")
    transcript = r.recognize_google(audio)
  except s_r.UnknownValueError:
    transcript = "Unable to recognize speech"

  print(transcript) #to print voice into text
  speak_transcript(transcript)

  if 'lullaby' in transcript:
    play_lullaby()
  if 'stop' in transcript:
    # Kill player
  if 'exit' in transcript or 'quit' in transcript:
    exit()
