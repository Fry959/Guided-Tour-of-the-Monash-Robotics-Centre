import sys
sys.path.insert(0,'C:\\Users\\User\\Desktop\\FYP\\pynaoqi-python2.7-2.5.5.5-win32-vs2013\\lib')
import qi
import argparse
import time
from naoqi import ALProxy
Navigation = ALProxy("ALNavigation", "160.69.69.101", 9559)
tts = ALProxy("ALTextToSpeech", "160.69.69.101", 9559)
Motion = ALProxy("ALMotion", "160.69.69.101", 9559)
def main (session):
    
    motion.wakeUp()

    tts.say("Hello, let us begin the tour")
    tts.say("Follow me")


    sys.exit(1)
main (session)
