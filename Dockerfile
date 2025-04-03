FROM ros:noetic-ros-base-focal
COPY . /opt/barracuda-manipulator
SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -y \
    git \
    openssh-client \
    vim \
    #i2c-tools \
    #python3-pandas \
    #python3-numpy \
    python3-rospy \
    python3-pip \
    python3-ri.gpio \ 
    && pip3 install --no-cache-dir smbus2 \
    && apt-get purge -y python3-pip \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x /opt/barracuda-manipulator/entrypoint.sh \
    && mkdir /root/.ssh && chmod 700 /root/.ssh \
    && ssh-keyscan github.com >> /root/.ssh/known_hosts \
    && git config --global url."git@github.com:".insteadOf "https://github.com/" \
    && echo "source /opt/ros/noetic/setup.bash" >> /root/.bashrc \
    && echo "[ -f /opt/barracuda-manipulator/catkin_ws/devel/setup.bash ] && source /opt/barracuda-manipulator/catkin_ws/devel/setup.bash" >> /root/.bashrc \ 
    && echo "cd /opt/barracuda-manipulator/catkin_ws" >> /root/.bashrc
    
WORKDIR /opt/barracuda-manipulator/catkin_ws/
CMD ["/opt/barracuda-manipulator/entrypoint.sh"]