import setup_path
import airsim

import numpy as np
import os
import tempfile
import pprint
import cv2
import math

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.simEnableWeather(True)


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

airsim.wait_key('Press any key to enable fog at 75%')

client.simSetWeatherParameter(airsim.WeatherParameter.Fog, 0.75);

print("Taking off...")
client.armDisarm(True)
client.takeoffAsync().join()

print("Take off position is ", client.simGetVehiclePose(vehicle_name="FishEyeDrone").position)

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))


airsim.wait_key('Press any key to enable snow at 50%')
print('set all effects to 0%')
client.simSetWeatherParameter(airsim.WeatherParameter.Fog, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.Snow, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.MapleLeaf, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.Snow, 0.75);
print('move vehicle to (-10, 10, -10) at 5 m/s')
client.moveToPositionAsync(-10, 10, -10, 5).join()


client.hoverAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))


airsim.wait_key('Press any key to enable maple leaves at 50%')
print('set all effects to 0%')
client.simSetWeatherParameter(airsim.WeatherParameter.Fog, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.Snow, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.MapleLeaf, 0.0);
client.simSetWeatherParameter(airsim.WeatherParameter.MapleLeaf, 0.50);
print('reset to original state')
#camera_pose = airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(math.radians(15), 0, 0)) #radians
#client.simSetCameraPose("0", camera_pose)

client.moveToPositionAsync(0.0, 0.0, -1, 5).join()
client.armDisarm(False)

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)
