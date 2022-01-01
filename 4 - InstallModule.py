"""
--> pyttsx3 
    is a external  module which was installed by me by using
    command "pip install pyttsx3"
    in command prompt and then it was installed automatically...

    the syntax of this code is fixed and i found that on google...
    this is example of external module, one can use this to make a jarvis
    type program and not only this there are lots of more module available
    on internet...

"""

#this line will import the module
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello henil! I am the text to speech module called pyttsx3 and i was installed manually because i am not the in-built module.")

#without this line the speech will never be spoken...
engine.runAndWait()


"""
--> Changing the voice....
    here you change the volume whether you want female or male voice
    it is upto you...

    (*) use 0 for male and 1 for female... 
"""

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello henil! i am your female voice assistant.")
engine.runAndWait()

"""
--> Volume and rate
    --> you can also change and set the volume and speech rate of 
    voice by similar functions...
    as we have done for voice...
"""

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.say("My current speech rate is "+str(rate)+" and my current volume is "+str(volume))
engine.runAndWait()

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.5)
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.say("Soorry lady because you're wrong! i have updated the settings for you sir! NOW, the speaking rate is "+str(rate)+" and volume is "+str(volume))
engine.runAndWait()