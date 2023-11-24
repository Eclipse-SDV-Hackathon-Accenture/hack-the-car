# Protobuf interfaces of the test vehicle

---

### Turn indicator contol
|   |  |
| --- | --- |
| File     | [Arbitration/IndicatorRequest.proto](/datatypes/Arbitration/IndicatorRequest.proto) |
| Message | **pb.Arbitration.IndicatorRequest** |
| Direction | To vehicle |
| Topic  | TurnIndicatorRequestArbitrated |

---

### Various in-vehicle buttons 
|   |  |
| --- | --- |
| File     | [SensorNearData/CarSwitches.proto](/datatypes/SensorNearData/CarSwitches.proto) |
| Message | **pb.SensorNearData.CarSwitches** |
| Direction | From vehicle |
| Topic  | CarSwitchesInPb |

---

### Gas pedal position and gear
|   |  |
| --- | --- |
| File     | [SensorNearData/PowerTrain.proto](/datatypes/SensorNearData/PowerTrain.proto) |
| Message | **pb.SensorNearData.PowerTrain** |
| Direction | From vehicle |
| Topic  | PowerTrainInPb |

---

### Brake pedal pressure
|   |  |
| --- | --- |
| File     | [SensorNearData/Brake.proto](/datatypes/SensorNearData/Brake.proto) |
| Message | **pb.SensorNearData.Brake** |
| Direction | From vehicle |
| Topic  | BrakeInPb |

---

### Steering wheel angle, speed per wheel and IMU data
|   |  |
| --- | --- |
| File     | [SensorNearData/VehicleDynamics.proto](/datatypes/SensorNearData/VehicleDynamics.proto) |
| Message | **pb.SensorNearData.VehicleDynamics** |
| Direction | From vehicle |
| Topic  | VehicleDynamicsInPb |

---

### GPS position
|   |  |
| --- | --- |
| File     | [ros/sensor_msgs/NavSatFix.proto](/datatypes/ros/sensor_msgs/NavSatFix.proto) |
| Message | **ros.sensor_msgs.NavSatFix** |
| Direction | From vehicle |
| Topic  | ROSGlobalPosition |

---

### Camera image
|   |  |
| --- | --- |
| File     | [ros/sensor_msgs/CompressedImage.proto](/datatypes/ros/sensor_msgs/CompressedImage.proto) |
| Message | **ros.sensor_msgs.CompressedImage** |
| Direction | From vehicle |
| Topic  | ROSFrontCenterImage |

---

### LIDAR point cloud
|   |  |
| --- | --- |
| File     | [ros/sensor_msgs/PointCloud2.proto](/datatypes/ros/sensor_msgs/PointCloud2.proto) |
| Message | **ros.sensor_msgs.PointCloud2** |
| Direction | From vehicle |
| Topic  | ROSVLS128CenterCenterRoof |

---

### Detected traffic participants
|   |  |
| --- | --- |
| File     | [ros/visualization_msgs/MarkerArray.proto](/datatypes/ros/visualization_msgs/MarkerArray.proto) |
| Message | **ros.visualization_msgs.MarkerArray** |
| Direction | From vehicle |
| Topic  | ROSTrafficParticipantList |
