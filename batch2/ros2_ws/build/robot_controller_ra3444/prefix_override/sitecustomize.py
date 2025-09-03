import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/administrator/dhina/DhinaKunal/batch2/ros2_ws/install/robot_controller_ra3444'
