#!/usr/bin/env python 
import rospy
from sensor_msgs.msg import LaserScan
 
def callback_laser(msg): # callback function for subscriber
    # divide total laser scan of 180 degrees into 5 parts
    regions = [ 
      min(msg.ranges[0:143],10),
      min(msg.ranges[144:287],10),
      min(msg.ranges[288:431],10),
      min(msg.ranges[432:575],10),
      min(msg.ranges[576:713],10),
     ]
    rospy.loginfo(regions)
 
def main():
    rospy.init_node('reading_laser')
    rospy.Subscriber("/obst_avoidance_robot/laser/scan", LaserScan, callback_laser)
    rospy.spin()
 
if __name__ == '__main__':
    main()