# Daniel's 2024 Summer Research Project
## AirSim Settings
```
{
	"SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/main/docs/settings.md",
	"SettingsVersion": 1.2,
	"SimMode": "Multirotor", #sim mode is for Drone only
	"ClockSpeed": 1,
	"ViewMode": "FlyWithMe",
	"Vehicles": {
		"FishEyeDrone": {   # Vehicle name
			"VehicleType": "SimpleFlight",
			"EnableCollisionPassthrogh": false,
			"EnableCollisions": true,
			"Cameras": { # use 3 cameras come with drone
				"bottom-center": {
					"CaptureSettings": [
						{
							"ImageType": 0,
							"Width": 1920,
							"Height": 1080,
							"FOV_Degrees": 90
						}
					],
					"X": 0, "Y": 0,	"Z": 0,
					"Pitch": -90, "Roll": 0.0, "Yaw": 0.0
				},
				"front-left": {
					"CaptureSettings": [
						{
							"ImageType": 0,
							"Width": 672,
							"Height": 376,
							"FOV_Degrees": 90
						}
					],
					"X": 0.50, "Y": -20.0, "Z": 0.10,
					"Pitch": 0.0, "Roll": 0.0, "Yaw": 0.0
				},
				"front-right": {
					"CaptureSettings": [
						{
							"ImageType": 0,
							"Width": 672,
							"Height": 376,
							"FOV_Degrees": 90
						}
					],
					"X": 0.50, "Y": 20.0, "Z": 0.10,
					"Pitch": 0.0, "Roll": 0.0, "Yaw": 0.0
				}
			},
			"Gimbal": {
				"Stabilization": 1,
				"Pitch": -90,
				"Roll": 0,
				"Yaw": 0
			},
			"X": 0, "Y": 0, "Z": 0,
			"Pitch": 0, "Roll": 0, "Yaw": 0
		}
	},
	"SubWindows": [ # each subwindow use one earlier defined camera
		{
			"WindowID": 0,
			"ImageType": 0,
			"CameraName": "bottom-center",
			"Visible": true
		},
		{
			"WindowID": 1,
			"ImageType": 0,
			"CameraName": "front-right",
			"Visible": true
		},
		{
			"WindowID": 2,
			"ImageType": 0,
			"CameraName": "front-left",
			"Visible": true
		}
	],
	"Recording": {
		"RecordOnMove": false,
		"RecordInterval": 0.05,
		"Folder": "",
		"Enabled": false,
		"Cameras": [
			{
				"CameraName": "bottom-center",
				"ImageType": 0,
				"PixelsAsFloat": false,
				"VehicleName": "FishEyeDrone",
				"Compress": true
			}
		]
	}
}

```

## Simulation Implementation

### Simulate Drone Landing (hello_drone_landing.py)
Drone take off and land at the same spot
* Drone take off and get take off position
* Drone fly to a different spot 
* Drone land back to the take off spot

### SimulateWeather Change (hello_drone_weather.py)
Use weather API to change weather during the drone flying trip. 
* Drone take off set weather to Fog 
* Drone fly set weather to Snow 
* Drone land set weater to Leaf

### Simulate Windy Weather (hello_drone_wind.py)
Use wind API to change wind speed during the drone flying trip
* Drone take off set wind to 15m/s towards right 
* Drone Fly set wind to 0 
* Drone landing set wind to 10m/s in forward direction



# Python API for AirSim

This package contains Python APIs for [AirSim](https://github.com/microsoft/airsim).

## How to Use
See examples at [car/hello_car.py](https://github.com/Microsoft/AirSim/blob/main/PythonClient/car/hello_car.py) or [multirotor/hello_drone.py](https://github.com/microsoft/AirSim/blob/main/PythonClient/multirotor/hello_drone.py).

## Dependencies
This package depends on `msgpack` and would automatically install `msgpack-rpc-python` (this may need administrator/sudo prompt):
```
pip install msgpack-rpc-python
```

Some examples also requires opencv.

## More Info

More information on AirSim Python APIs can be found at:
https://github.com/Microsoft/AirSim/blob/main/docs/python.md


