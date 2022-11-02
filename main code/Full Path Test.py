import sys
sys.path.insert(0,'C:\\Users\\User\\Desktop\\FYP\\pynaoqi-python2.7-2.5.5.5-win32-vs2013\\lib')
import qi
import argparse
import time
import math
from naoqi import ALProxy


##life_awareness = ALProxy("ALAutonomousLife", "160.69.69.101", 9559)
##life_awareness.setAutonomousAbilityEnabled("BasicAwareness", False)
tts = ALProxy("ALTextToSpeech", "160.69.69.101", 9559)
motion = ALProxy("ALMotion", "160.69.69.101", 9559)
animation= ALProxy("ALAnimationPlayer","160.69.69.101", 9559)
#motion.rest()
motion.wakeUp()
time.sleep(1)
motion.setOrthogonalSecurityDistance(0.10) #These two lines sets the security distances os the robot
motion.setTangentialSecurityDistance(0.11) #Set to minimum
animation.run("animations/Stand/Gestures/YouKnowWhat_1")
tts.say("Hello....Welcome to the guided tour")
tts.say("I am Pepper and I will show you my friends around the robotics centre")
tts.say("Follow me")

right = -math.pi/2
left = math.pi/2
reverse = math.pi

motion.moveTo(-0.2,0,0)
motion.moveTo(0,0,reverse)
##motion.moveTo(0.9,0,0)
##motion.moveTo(0,0,right)
motion.moveTo(1.3,0,0)
motion.moveTo(0,0,right)
tts.say("This is the main corridor")
time.sleep(1)
motion.moveTo(3,0,0)
tts.say("To my left are Jackal and Fetch")
motion.moveTo(0,0,left)
tts.say("Jackal is an autonomous robot for the outdoors")
tts.say("It is a fast four by four car and is waterproof")
tts.say("Jackal is being used to develop pedestrian detection algorithms")
time.sleep(0.5)
tts.say("The big white robot is Fetch")
tts.say("Fetch has 7 degrees of freedom")
tts.say("He can pick up all sorts of things with his gripper")
tts.say("He gets used for a lot of research")
tts.say("He is used to pick up balls and small objects upto 6 kilograms")
tts.say("He is a favourite in every lab for research in automation")
motion.moveTo(0,0,right)
motion.post.moveTo(4,0,0)
tts.say("This is where I sleep after a hard days work ")
#turn right into path to PANDA arm
motion.moveTo(4,0,0)
motion.moveTo(0,0,right)
motion.moveTo(4.4,0,0)
motion.moveTo(0,0,right)
motion.moveTo(5,0,0)
motion.moveTo(0,0,left)
motion.moveTo(2,0,0)
tts.say("This is Panda")
tts.say("Panda is a robotic arm with 7 degrees of freedom")
tts.say("It acts like a human arm and can lift up to 3 kilograms")
tts.say("Panda has force sensors to detect objects within its gripper")
tts.say("It is used for research in manipulator control")
tts.say("It can also be used for manufacturing tasks")
motion.moveTo(0,0,reverse)
motion.moveTo(2,0,0)
motion.moveTo(0,0,right)
#enter secondary corridor towards Baxter
#motion.moveTo(13.5,0,0)
i = 1
while i < 7:
motion.moveTo(2,0,0)
break
motion.moveto(0.5,0)
motion.moveTo(0,0,right)
motion.moveTo(1,0,0)
tts.say("This is Baxter")
tts.say("Baxter has 360 degree vision and can detect humans")
tts.say("Baxter is used to automate low complexity production tasks in small factories")
tts.say("The LCD head allows Baxter to display emotions and communicate with the user")
motion.moveTo(0,0,reverse)
motion.moveTo(1,0,0)
motion.moveTo(0,0,right)
motion.moveTo(12.3,0,0)
motion.moveTo(0,0,left)
motion.moveTo(4.5,0,0)
motion.moveTo(0,0,right)
motion.moveTo(2,0,0)
motion.moveTo(0,0,right)
tts.say("This is Panda 2")
tts.say("It uses Desk, a browser based interface for control")
motion.moveTo(0,0,right)
#Return to start position near G90B
while i < 26:
motion.moveTo(2,0,0)
break
tts.say("The tour is over")
tts.say("Thank you for coming")

