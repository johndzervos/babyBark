import speech_recognition as s_r
import vlc
import os

import asyncio
import time

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
    transcript = r.recognize_google(audio)
  except s_r.UnknownValueError:
    transcript = "Unable to recognize speech"

  print(transcript) #to print voice into text

  if 'lullaby' in transcript:
    play_lullaby()
  if 'exit' in transcript or 'quit' in transcript:
    exit()
