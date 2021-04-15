#!/usr/bin/env python3
import roslib
import rospy
from sensor_msgs.msg import Imu, MagneticField
from std_msgs.msg import Header
from geometry_msgs.msg import Vector3

import board
import busio

import adafruit_fxos8700
import adafruit_fxas21002c


def talker():
    # Initialize I2C bus and device.
    i2c = busio.I2C(board.SCL, board.SDA)

    # sensor_am = adafruit_fxos8700.FXOS8700(i2c)
    # Optionally create the sensor with a different accelerometer range (the
    # default is 2G, but you can use 4G or 8G values):
    sensor_am = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_4G)
    # sensor_am = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_8G)

    # sensor_g = adafruit_fxas21002c.FXAS21002C(i2c)
    # Optionally create the sensor with a different gyroscope range (the
    # default is 250 DPS, but you can use 500, 1000, or 2000 DPS values):
    # sensor_g = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_500DPS)
    sensor_g = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_1000DPS)
    # sensor_g = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_2000DPS)

    pub = rospy.Publisher("imu_raw_accel_gyro", Imu, queue_size=1)
    pub_mag = rospy.Publisher("imu_raw_mag", MagneticField, queue_size=1)
    rospy.init_node("imu_raw")

    msg = Imu()
    msg.angular_velocity = Vector3()
    msg.linear_acceleration = Vector3()
    msg.linear_acceleration_covariance = [0.0001, 0,      0,
                                          0,      0.0001, 0,
                                          0,      0,      0.0001]
    msg.angular_velocity_covariance    = [0.0001, 0,      0,
                                          0,      0.0001, 0,
                                          0,      0,      0.0001]

    msg_mag = MagneticField()
    msg_mag.magnetic_field = Vector3()
    msg_mag.magnetic_field_covariance  = [9, 0, 0,
                                          0, 9, 0,
                                          0, 0, 9]

    msg.header.frame_id = "imu_link"
    msg_mag.header.frame_id = "imu_link"

    rospy.loginfo("IMU node ready!")

    while not rospy.is_shutdown():
        # Read acceleration & magnetometer
        accel_x, accel_y, accel_z = sensor_am.accelerometer
        mag_x, mag_y, mag_z = sensor_am.magnetometer
        # Read gyroscope
        gyro_x, gyro_y, gyro_z = sensor_g.gyroscope

        msg.angular_velocity.x = gyro_x
        msg.angular_velocity.y = gyro_y
        msg.angular_velocity.z = gyro_z

        msg.linear_acceleration.x = accel_x
        msg.linear_acceleration.y = accel_y
        msg.linear_acceleration.z = accel_z

        msg_mag.magnetic_field.x = mag_x
        msg_mag.magnetic_field.y = mag_y
        msg_mag.magnetic_field.z = mag_z

        msg.header.stamp = rospy.Time.now()
        msg_mag.header.stamp = rospy.Time.now()

        pub.publish(msg)
        pub_mag.publish(msg_mag)
        rospy.sleep(0.002)


if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
