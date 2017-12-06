#!/usr/bin/python
import rospy
from geometry_msgs.msg import Pose
from random import random

rospy.init_node('CNCgoal_pub')
pub=rospy.Publisher('/CNC/pose',Pose,queue_size=1)
rate=rospy.Rate(.2)

while not rospy.is_shutdown():
    goal=Pose()
    goal.position.x=random()
    goal.position.y=random()
    goal.position.z=random()
    pub.publish(goal)
    rate.sleep()
