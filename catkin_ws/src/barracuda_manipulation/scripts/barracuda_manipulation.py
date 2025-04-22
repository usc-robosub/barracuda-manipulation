#!/usr/bin/env python3
import rospy
from std_reqs.req import Bool
# import board
import RPi.GPIO as GPIO
import time

'''
Solenoids:
-grabber
-dropper
-torpedo launcher
-Extra fourth
'''

# Pin numbers (may change later)
GRABBER_PIN = 17
DROPPER_PIN = 27
TORPEDO_PIN = 22
FOURTH_PIN = 23

# Subscriber callback functions
# Note: check if active high or active low
# Also check to see if we want the callback functions to set the pins 
# high and low by themselves, or if we will be sending another signal to turn them off
# (would make sense to do it separately?)

def grabber_control_handler(req):
    if req.status:
        GPIO.output(GRABBER_PIN, GPIO.HIGH)
        rospy.loginfo("setting grabber high")
    else: 
        GPIO.output(GRABBER_PIN, GPIO.LOW)
        rospy.loginfo("setting grabber low")

def dropper_control_handler(req):
    if req.status:
        GPIO.output(DROPPER_PIN, GPIO.HIGH)
        rospy.loginfo("setting dropper high")
    else: 
        GPIO.output(DROPPER_PIN, GPIO.LOW)
        rospy.loginfo("setting dropper low")

def torpedo_control_handler(req):
    if req.status:
        GPIO.output(TORPEDO_PIN, GPIO.HIGH)
        rospy.loginfo("setting torpedo high")
    else: 
        GPIO.output(TORPEDO_PIN, GPIO.LOW)
        rospy.loginfo("setting torped low")

def fourth_control_handler(req):
    if req.status:
        GPIO.output(FOURTH_PIN, GPIO.HIGH)
        rospy.loginfo("setting fourth high")
    else: 
        GPIO.output(FOURTH_PIN, GPIO.LOW)
        rospy.loginfo("setting foruth low")


# can I chose the topic names, or am I making them up
def manipulator_node():

    GPIO.setmode(GPIO.BCM)  # check if BCM mode
    GPIO.setup(GRABBER_PIN, GPIO.OUT)
    GPIO.setup(DROPPER_PIN, GPIO.OUT)
    GPIO.setup(TORPEDO_PIN, GPIO.OUT)
    GPIO.setup(FOURTH_PIN, GPIO.OUT)

    # rospy.init_node('manipulator', anonymous=True) # Check to see if anonymous is needed
    # rospy.Subscriber('/manipulator/grabber/state', Bool, grabber_control)
    # rospy.Subscriber('/manipulator/dropper/state', Bool, dropper_control)
    # rospy.Subscriber('/manipulator/torpedo/state', Bool, torpedo_control)
    # rospy.Subscriber('/manipulator/fourth/state', Bool, fourth_control)

    grabber_service = rospy.service('grabber_control', SetPin, grabber_control_handler)
    dropper_service = rospy.service('dropper_control', SetPin, dropper_control_handler)
    torpedo_service = rospy.service('torpedo_control', SetPin, torpedo_control_handler)
    fourth_pin_service = rospy.service('fourth_control', SetPin, fourth_control_handler)

    rospy.on_shutdown(GPIO.cleanup)    
    rospy.spin()

if __name__ == '__main__':
    manipulator_node()