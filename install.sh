#!/bin/sh
echo "Updating and installing python libraries."
apt-get update
apt-get install python3-picamera
pip install sendgrid

echo "Downloading and installing prebuilt ffmpeg."
wget https://github.com/ccrisan/motioneye/wiki/precompiled/ffmpeg_2.8.3.git325b593-1_armhf.deb
dpkg -i ffmpeg_2.8.3.git325b593-1_armhf.deb

echo "Removing previous ffmpeg."
apt-get remove libavcodec-extra-56 libavformat56 libavresample2 libavutil54
apt-get install libavutil54 libavformat56 libswscale3
echo "Downloading Mr Dave's version of motion."
wget https://github.com/ccrisan/motioneye/wiki/precompiled/motion-mrdave-raspbian -O /usr/local/bin/motion
chmod +x /usr/local/bin/motion

echo "Installing the dependencies."
apt-get install python-pip python-dev curl libssl-dev libcurl4-openssl-dev libjpeg-dev
pip install motioneye

echo "Preparing the configuration directory."
mkdir -p /etc/motioneye
cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

echo "Preparing the media directory."
mkdir -p /var/lib/motioneye

echo "Make motioneye start on boot."
cp init-motion-server.sh /etc/init.d/init-motion-server.sh
sudo update-rc.d init-motion-server.sh defaults

echo "Allowing use of CSI camera module."
if !grep -Fxq "bcm2835-v4l2" /etc/modules
then
	echo 'bcm2835-v4l2' >> /etc/modules
fi
