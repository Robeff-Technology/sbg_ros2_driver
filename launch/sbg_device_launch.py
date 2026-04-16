import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
	frame_id = LaunchConfiguration('frame_id')

	config = os.path.join(
		get_package_share_directory('sbg_driver'),
		'config',
		'sbg_device_uart_default.yaml'
	)

	return LaunchDescription([
		DeclareLaunchArgument(
			'frame_id',
			default_value='imu_link_ned',
			description='ROS header frame_id for SBG output messages'
		),
		Node(
			package='sbg_driver',
		#	name='sbg_device_1',
			executable = 'sbg_device',
			output = 'screen',
			parameters = [
				config,
				{'output.frame_id': frame_id}
			]
		)
	])
