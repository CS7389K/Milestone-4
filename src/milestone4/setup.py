from setuptools import setup

package_name = 'milestone4'

setup(
    name=milestone4,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Andrew Scouten',
    maintainer_email='yzb2@txstate.edu',
    description='Real-time object detection using the YOLO model with the TurtleBot3.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = milestone4.publisher:main',
            'listener = milestone4.subscriber:main',
        ],
    },
)
