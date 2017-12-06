#!/usr/bin/python
import rospy
from cnc_utils import CNC
from geometry_msgs.msg import Pose

class CNCSerial(object):
   def __init__(self,port="/dev/ttyACM0"):
      self.CNC=CNC(port, homing=False)
      self.sub = rospy.Subscriber('/CNC/pose', Pose, self.pose_callback, queue_size=1)

   def pose_callback(self, msg):
   	  pose=msg
   	  self.CNC.send_cmd("g0x%sy%sz-%s"%(pose.position.x,pose.position.y,pose.position.z))

if __name__ == "__main__":
    rospy.init_node('cnc_serial')
    cnc_serial = CNCSerial()
    rospy.spin()
