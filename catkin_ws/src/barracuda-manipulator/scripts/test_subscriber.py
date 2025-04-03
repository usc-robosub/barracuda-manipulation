#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool
import time

def test_publisher_node():
    rospy.init_node('manipulator_test_publisher')

    # Publishers for each solenoid
    grabber_pub = rospy.Publisher('/manipulator/grabber/state', Bool, queue_size=10)
    dropper_pub = rospy.Publisher('/manipulator/dropper/state', Bool, queue_size=10)
    torpedo_pub = rospy.Publisher('/manipulator/torpedo/state', Bool, queue_size=10)
    fourth_pub = rospy.Publisher('/manipulator/fourth/state', Bool, queue_size=10)

    rospy.sleep(1)  # Give time for subscribers to connect

    rate = rospy.Rate(0.5)  # 0.5 Hz = 2 seconds per cycle

    while not rospy.is_shutdown():
        for pub, name in zip([grabber_pub, dropper_pub, torpedo_pub, fourth_pub], 
                             ["grabber", "dropper", "torpedo", "fourth"]):
            rospy.loginfo(f"Activating {name}")
            pub.publish(True)  # Turn on solenoid
            time.sleep(2)  # Wait 2 seconds

            rospy.loginfo(f"Deactivating {name}")
            pub.publish(False)  # Turn off solenoid
            time.sleep(2)  # Wait 2 seconds

        rate.sleep()

if __name__ == '__main__':
    try:
        test_publisher_node()
    except rospy.ROSInterruptException:
        pass