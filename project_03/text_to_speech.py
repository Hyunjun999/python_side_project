# library version: playsound==1.2.2
from gtts import gTTS
from playsound import (
    playsound,
)  # If you are using macos or unix/linux system,

# you have to install pip install PyObjC package as well to avoid the error from the playsound.
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# __file__ : current python file
# os.path.abspath(__file__) : current python file's abs path
# os.path.dirname(os.path.abspath(__file__)) : get the dir name of the current python file's abs path
# os.chdir(os.path.dirname(os.path.abspath(__file__))) : change dir to where the current python file is wherever you execute it.
file_path = "text.txt"
with open(file_path, "rt", encoding="utf-8") as f:
    read_file = f.read()
tts = gTTS(text=read_file, lang="ko")
tts.save("hi.mp3")
playsound("hi.mp3")
