#!/usr/bin/env python3
import roslib
import rospy
from sensor_msgs.msg import NavSatFix, NavSatStatus
from std_msgs.msg import Header

import io
import pynmea2
import serial

ser = serial.Serial('/dev/ttyTHS0', 9600, timeout=1)
sio = io.TextIOWrapper(io.BufferedReader(ser))

def talker():
    pub = rospy.Publisher('gps_data', NavSatFix)
    rospy.init_node('gps')

    msg = NavSatFix()
    msg.status = NavSatStatus(0, 0x1 | 0x2) # Unaugmented fix, GPS & GLONASS

    while not rospy.is_shutdown():
        try:
            line = sio.readline()
            if not line: continue
            gpsmsg = pynmea2.parse(line)
            if type(gpsmsg) == pynmea2.GGA:
                qual = gpsmsg.gps_qual
                if qual > 0: # Valid gps fix?
                    msg.status.status = qual - 1 if qual <= 2 else 2 # See sensor_msgs/NavSatStatus
                    msg.latitude = gpsmsg.latitude
                    msg.longitude = gpsmsg.longitude
                    msg.altitude = gpsmsg.altitude
                    # Send msg on topic
                    pub.publish(msg)
            
        except serial.SerialException as e:
            rospy.logerr('Device error: {}'.format(e))
            break
        except pynmea2.ParseError as e:
            rospy.logerr('Parse error: {}'.format(e))
            continue
        except UnicodeDecodeError:
            continue

        msg.header.stamp = rospy.Time.now()

        pub.publish(msg)
        rospy.sleep(0.001)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass