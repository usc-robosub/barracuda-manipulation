source /opt/ros/noetic/setup.bash
[ -f /opt/barracuda-manipulation/catkin_ws/devel/setup.bash ] && source /opt/barracuda-manipulation/catkin_ws/devel/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source /opt/barracuda-manipulation/catkin_ws/devel/setup.bash" >> ~/.bashrc
roslaunch barracuda_manipulation manipulation_test.launch # --wait

# exec tail -f /dev/null