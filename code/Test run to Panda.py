import sys
sys.path.insert(0,'C:\\Users\\User\\Desktop\\FYP\\pynaoqi-python2.7-2.5.5.5-win32-vs2013\\lib')
import qi
import argparse
import time
import math
from naoqi import ALProxy


tts = ALProxy("ALTextToSpeech", "160.69.69.101", 9559)
motion = ALProxy("ALMotion", "160.69.69.101", 9559)
tts.say("Welcome to the guided tour")
tts.say("Follow me")
theta = -math.pi/2
#theta = 3.1415/2
motion.wakeUp()

#motion.moveTo(1,0,0) #exit G90B
#motion.moveTo(0,0,theta) #assuming that 90 degree turn is always to the right
##motion.moveTo(1.2,0,0) #reach main corridor
##motion.moveTo(0,0,theta)
##motion.moveTo(3,0,0) #move towards Fetch
tts.say("This is Fetch")
motion.moveTo(2,0,0) #move to main hallway
motion.moveTo(2,0,0)
motion.moveTo(2,0,0)
motion.moveTo(2,0,0)
motion.moveTo(2,0,0)
motion.moveTo(0.7,0,0)
motion.moveTo(0,0,theta) #turn to go towards Panda robot arm
motion.moveTo(2,0,0)
motion.moveTo(1,0,0)
motion.moveTo(1.2,0,0)

motion.moveTo(0,0,theta)
motion.moveTo(2,0,0)
motion.moveTo(2,0,0)
motion.moveTo(1,0,0)
motion.moveTo(0,0,-theta) #turn 90 degrees to the left
motion.moveTo(2,0,0)
tts.say("This is the PANDA arm")
