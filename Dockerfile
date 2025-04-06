FROM ros:noetic-ros-base-focal
COPY . /opt/barracuda-manipulation
SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -y \
    python3-catkin-tools \
    ros-noetic-catkin \
    # git \
    # openssh-client \
    vim \
    #i2c-tools \
    #python3-pandas \
    #python3-numpy \
    python3-rospy \
    python3-pip \
    && pip3 install --no-cache-dir RPi.GPIO smbus2 \ 
    && apt-get purge -y python3-pip \ 
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x /opt/barracuda-manipulation/entrypoint.sh
    # && mkdir /root/.ssh && chmod 700 /root/.ssh \
    #&& ssh-keyscan github.com >> /root/.ssh/known_hosts \
    # && git config --global url."git@github.com:".insteadOf "https://github.com/" \
    # && echo "source /opt/ros/noetic/setup.bash" >> /root/.bashrc \
    # && echo "[ -f /opt/barracuda-manipulation/catkin_ws/devel/setup.bash ] && source /opt/barracuda-manipulation/catkin_ws/devel/setup.bash" >> /root/.bashrc \ 
    # && echo "cd /opt/barracuda-manipulation/catkin_ws" >> /root/.bashrc

WORKDIR /opt/barracuda-manipulation/catkin_ws/
RUN . /opt/ros/noetic/setup.sh \
    && cd /opt/barracuda-manipulation/catkin_ws \
    && catkin_make

CMD ["/opt/barracuda-manipulation/entrypoint.sh"]

# pip3 purge line keeps Docker image smaller