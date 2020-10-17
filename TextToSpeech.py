# pip install gTTS 
# pip install playsound


from gtts import gTTS
from playsound import playsound

#Natural Language Processing in Hindi

# Defining speech variable (What you want to hear from the machine)
user_speech = '''Hello, my name is GitHub and I am contributing in this repo '''

# Defining speech parameters for English Language
# objective = gTTS(text = user_speech, slow = False, lang = "en")


# Defining speech parameters for hindi language
objective = gTTS(text = user_speech, slow = False, lang = "hi")

# Saving the speech
objective.save("synthesis_hindi.mp3")

# Say it aloud
playsound("synthesis_hindi.mp3")
