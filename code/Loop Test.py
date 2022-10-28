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
theta = -math.pi/2 #anti-clockwise is positive so to turn right, need negative
#theta = 3.1415/2
#rotright = 1.571
#rotleft = -1.571
motion.wakeUp()

#Move Pepper to do 1m square loop to starting point
#test to ensure Pepper always turns to the right
motion.moveTo(1,0,0)
motion.moveTo(0,0,theta)
motion.moveTo(1,0,0)
motion.moveTo(0,0,theta)
motion.moveTo(1,0,0)
motion.moveTo(0,0,theta)
motion.moveTo(1,0,0)

#Now test to see how Pepper turns left
#motion is 1m forward, then turn left, then 1m forward

#motion.moveTo(1,0,0)
#motion.moveTo(0,0,-theta) #turning left because theta is negative
