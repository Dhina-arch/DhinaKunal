#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# Base class
class MyNode(Node):
    def __init__(self, mammalName):
        super().__init__('my_node')  # Initialize the ROS 2 node
        print(mammalName, 'is warm-blooded animal')

# Subclass of MyNode
class Dog(MyNode):
    def __init__(self):
        super().__init__('Dog')  # Call MyNode constructor with 'Dog'
        print('Dog has four legs')

# Main function
def main(args=None):
    rclpy.init(args=args)

    dog = Dog()               # Create instance (which is a Node)
    rclpy.spin(dog)           # Keep the node alive

    dog.destroy_node()
    rclpy.shutdown()

# Run main
if __name__ == '__main__':
    main()
