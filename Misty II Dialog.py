from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time
misty = Robot()
misty.start_face_recognition()

misty.move_arms(0,0)
misty.start_face_recognition()

def reaction_Max():
    misty.speak('Hi Max')
    misty.move_arms(0.-40,50,50)
    time.sleep(2)
    misty.move_arms(0.-40,50,50)
    time.sleep(2)

misty.start_key_phrase_recognition()
misty.change_led(255,0,0)
misty.create_conversation(name='Clirik', startingState='StartClirik',overwrite = True)
misty.create_state(name='StartClirik',speak ='Do you like colors?',contexts="['furhat.context.en.yes-no']", listen = True,noMatchSpeech='Couid you repeat that',repeatMaxCount=3,startAction='listen',overwrite=True)
misty.create_state(name='Yes', speak = 'I like  that one,which color do you  prefer betwen red,green or blue?',listen =True,noMatchSpeech= 'couid you repeat taht', repeatMaxCount=3,startAction ='admire',overwrite = True,contexts="['color_context_3_colors']")
misty.create_state(name='No', speak = 'Okey dont  paly  with me ttan ',listen =True,noMatchSpeech= 'couid you repeat taht', repeatMaxCount=3,startAction ='mad2',overwrite = True,)


misty.map_state(conversation='Clirik',state = 'StartClirik',trigger ='SpeechHeard',nextState='Yes',triggerFilter='yes',reEntry=False,overwrite=True)
misty.map_state(conversation='Clirik',state = 'StartClirik',trigger ='SpeechHeard',nextState='No',triggerFilter='no',reEntry=False,overwrite=True)

    
def Vitalik():
    misty.peak('Ohh Vitalik')
    misty.drive(-3,0)
    misty.display_imag('e_Fear.jpg',1)



def ff(data):
    print(data)
    global item 
    if ['massage']['label']=='Max':
        reaction_Max()
    else:
        Vitalik()
 

    

def Key(data):
    misty.change_led(0,255,0)
    misty.play_audio('s_PhraseHello.wav')
    time.sleep(2)
    misty.start_conversation('Clirik')

misty.register_event(event_name='ff',event_type=Events.FaceRecognition,callback_function=ff,keep_alive = False)
misty.keep_alive()
misty.register_event(event_name='GGGGG',event_type=Events.KeyPhraseRecognized,callback_function=Key,keep_alive =True)
misty.keep_alive()