import sys
sys.path.insert(0,'C:\\Users\\User\\Desktop\\FYP\\pynaoqi-python2.7-2.5.5.5-win32-vs2013\\lib')
import qi
import argparse
import time
from naoqi import ALProxy
#Test run to understand Pepper motion api
def main(session):

    motion  = session.service("ALMotion")
    posture = session.service("ALRobotPosture")
    tts = session.service("ALTextToSpeech")
    motion.wakeUp()

    tts.say("Hello, let us begin the tour")
    motion.moveTo(-1,0,0)
    theta = -1.571
   #motion.moveInit()

    #motion.moveTo(1.0, 0, theta) #test to see if simultaneous movement
    

    motion.post.moveTo(1.0, 0, 0) ##make Pepper move and talk at the same
    tts.say("I am moving")
    
    #Move Pepper to do 1m square loop to starting point
    #test to ensure Pepper always turns to the right
    motion.moveTo(1,0,0)
    motion.moveTo(0,0,theta)
    motion.moveTo(1,0,0)
    motion.moveTo(0,0,theta)
    motion.moveTo(1,0,0)
    motion.moveTo(0,0,theta)
    motion.moveTo(1,0,0)

    #this code ensures connection to robot, reconnects if Pepper loses connection midway                      
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="160.69.69.101",
                        help="Robot IP address. On robot or Local Naoqi: use '160.69.69.101'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
