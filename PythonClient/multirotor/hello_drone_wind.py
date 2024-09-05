import setup_path
import airsim

import numpy as np
import os
import tempfile
import pprint
import cv2
import math
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

client.armDisarm(True)

state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)

imu_data = client.getImuData()
s = pprint.pformat(imu_data)
print("imu_data: %s" % s)

barometer_data = client.getBarometerData()
s = pprint.pformat(barometer_data)
print("barometer_data: %s" % s)

magnetometer_data = client.getMagnetometerData()
s = pprint.pformat(magnetometer_data)
print("magnetometer_data: %s" % s)

gps_data = client.getGpsData()
s = pprint.pformat(gps_data)
print("gps_data: %s" % s)

airsim.wait_key('Press any key to set wind to 15m/s towards right')
wind = airsim.Vector3r(0, 15, 0)
client.simSetWind(wind)
print("Taking off...")
client.armDisarm(True)
client.takeoffAsync().join()
print("Take off position is ", client.simGetVehiclePose(vehicle_name="FishEyeDrone").position)

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key("Press any key to reset wind to 0")
wind = airsim.Vector3r(0, 0, 0)
client.simSetWind(wind)
print('Move vehicle to (-10, 10, -10) at 5 m/s')
client.moveToPositionAsync(-10, 10, -10, 5).join()

client.hoverAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))


airsim.wait_key("Press any key to set wind to 10m/s in forward direction") # NED
wind = airsim.Vector3r(10, 0, 0)
client.simSetWind(wind)
print('Reset to original state')
#camera_pose = airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(math.radians(15), 0, 0)) #radians
#client.simSetCameraPose("0", camera_pose)

client.moveToPositionAsync(0.0, 0.0, -1, 5).join()
client.armDisarm(False)

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)