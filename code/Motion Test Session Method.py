import sys
sys.path.insert(0,'C:\\Users\\User\\Desktop\\FYP\\pynaoqi-python2.7-2.5.5.5-win32-vs2013\\lib')
import qi
import argparse
import time
from naoqi import ALProxy

def main(session):

    motion  = session.service("ALMotion")
    posture = session.service("ALRobotPosture")
    tts = session.service("ALTextToSpeech")
    motion.wakeUp()

    tts.say("Hello, let us begin the tour")
    tts.say("Follow me")

  ##  motion.moveInit()

    motion.moveTo(1.0, 0, 0) ##move forward 1 metre
    time.sleep(0.5)

    motion.moveTo(0, 1, 1.5708) ##rotate 90 degrees and move 1m forward.
    motion.post.moveTo(1.0, 0, 0) ##move 1m 
    tts.say("I am moving")
    motion.rest()
    
##    motion.moveTo(0, 1.2, 1.5708)
##    motion.moveTo(0, 0, 1.5708)
##    motion.moveTo(0, 11.8, 0)
##    motion.moveTo(4.2, 0, 0)
    time.sleep(3)
                          
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="160.69.69.101",
                            help="Robot IP address. On robot or Local Naoqi: use '160.69.69.101")
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
