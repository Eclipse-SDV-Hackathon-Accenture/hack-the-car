import sys
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

# Import the "datatypes.ros.visualization_msgs.MarkerArray_pb2.py" file that we have just generated from the
# datatypes directory 
import datatypes.ros.visualization_msgs.MarkerArray_pb2 as MarkerArray

# Callback for receiving messages
def callback(topic_name, marker_array_proto_msg, time):
  ma = marker_array_proto_msg
  if(len(ma.markers) > 0):
    for var in ma.markers:
      if(var.ns == "pedestrian"):
        print("pedestrian")

if __name__ == "__main__":
  # initialize eCAL API. The name of our Process will be
  # "Python Protobuf Subscriber"
  ecal_core.initialize(sys.argv, "Python Protobuf Subscriber")

  # Create a Protobuf Publisher that publishes on the topic
  # "ROSTrafficParticipantList". The second parameter tells eCAL which
  # datatype we are expecting to receive on that topic.
  sub = ProtoSubscriber("ROSTrafficParticipantList"
                      , MarkerArray.MarkerArray)

  # Set the Callback
  sub.set_callback(callback)
  
  # Just don't exit
  while ecal_core.ok():
    time.sleep(2)
  
  # finalize eCAL API
  ecal_core.finalize()