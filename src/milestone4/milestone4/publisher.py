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

from std_msgs.msg import Float64, Int32

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
        self.bbox_x = self.create_publisher(Float64, 'bbox_x', 10)
        self.bbox_y = self.create_publisher(Float64, 'bbox_y', 10)
        self.bbox_w = self.create_publisher(Float64, 'bbox_w', 10)
        self.bbox_h = self.create_publisher(Float64, 'bbox_h', 10)
        self.clz = self.create_publisher(Int32, 'clz', 10)

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
        self.bbox_x.publish(Float64(data.bbox_x))
        self.bbox_y.publish(Float64(data.bbox_y))
        self.bbox_w.publish(Float64(data.bbox_w))
        self.bbox_h.publish(Float64(data.bbox_h))
        self.clz.publish(Int32(data.clz))
        self.get_logger().info('Publishing: "%s"' % str(data))


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