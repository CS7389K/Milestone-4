# Milestone 4

In this milestone, you will learn how to use YOLO, a real-time object detection algorithm based on a fully Convolutional Neural Network. YOLO’s input is a camera image fed in real time from a Raspberry Pi v2 camera, and the output would be a bounding box showing which part of the image belongs to which object, with a text label.

## Helpful Guides

### Foxy
- [Installation](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
- [Building Packages](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)
- [Publisher/Subscriber](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

### Ultralytics
- [YOLO](https://docs.ultralytics.com/)

## Development Environment

### Setup

1. Clone the repository
```sh
git clone https://github.com/CS7389K/Milestone-4.git
cd Milestone-4
```

2. ROS2 Foxy requires Ubuntu 20.04, so ensure it's what you're using. If you're using windows, run the following to use WSL:
```sh
install-wsl2-ros2-env.bat
```

3. Install Foxy
```sh
sh install-ros2-foxy-desktop.sh
```

### Building the Project

```sh
sh build.sh
. install/setup.sh
```
