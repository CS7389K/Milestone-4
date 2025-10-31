# Code taken from:
# https://github.com/ros2/examples/blob/fa10c22610648a90e7344cff4c27cd3356837543/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py#L1C1-L53C11
#
# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from .yolo_data import YOLOData


class YOLOPublisher(Node):
    """
    Publishes the following information:

        - Bounding box pixel location
        - Bounding box pixel width
        - Bounding box pixel height
        - Class information
        - Publishing the camera image is optional.

    Data Types: https://docs.ros2.org/foxy/api/std_msgs/index-msg.html
    """

    def __init__(
            self,
            publish_period : float = 0.5
        ):
        super().__init__('yolo_publisher')
        self.publisher = self.create_publisher(String, 'yolo_topic', 10)

    def publish(
            self,
            data: YOLOData
        ):
        # Ensure data has all required attributes
        assert hasattr(data, 'bbox_x')
        assert hasattr(data, 'bbox_y')
        assert hasattr(data, 'bbox_w')
        assert hasattr(data, 'bbox_h')
        assert hasattr(data, 'clz')
        # Publish data
        msg = String()
        msg.data = json.dumps(data.__dict__)
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % str(msg.data))


def main(args=None):
    rclpy.init(args=args)

    publisher = YOLOPublisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()