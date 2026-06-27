from playsound import playsound
import eel

# Function to play the assistant sound

@eel.expose
def playAssistantSound():
   music_dir = "www\\assets\\audio\\start_sound.mp3"
   playsound(music_dir)