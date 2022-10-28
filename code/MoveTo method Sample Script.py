import qi
import argparse
import sys
import math


def main(session):
    """
    This example uses the moveTo method.
    """
    # Get the services ALMotion & ALRobotPosture.

    motion_service  = session.service("ALMotion")
    

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Pose Init
    

    # Example showing the moveTo command
    # The units for this command are meters and radians
    x  = 1
    y  = 0
    theta  = 0
    motion_service.moveTo(x, y, theta)
    # Will block until move Task is finished

    ########
    # NOTE #
    ########
    # If moveTo() method does nothing on the robot,
    # read the section about walk protection in the
    # Locomotion control overview page.

    # Go to rest position
   # motion_service.rest()


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
