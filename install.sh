apt-get update
sudo apt-get install python3-picamera
apt-get remove libavcodec-extra-56 libavformat56 libavresample2 libavutil54
apt-get install libavutil54 libavformat56 libswscale3

apt-get install motion
apt-get install python-pip python-dev curl libssl-dev libcurl4-openssl-dev libjpeg-dev

pip install motioneye

mkdir -p /etc/motioneye
cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf

mkdir -p /var/lib/motioneye
