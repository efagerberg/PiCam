# PiCam
A python3 file that controls a Raspberry Pi camera, LEDs, and motion sensor.

# Install MotionEye
* Refer to `https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian`
* `sudo ./install.sh`
* Move init.sh to init folder

# Update motioneye
* `sudo ./upgrade.sh`

# Configure Sendgrid
Make an account and generate a free API Key
`https://sendgrid.com/free/?source=sendgrid-python`

Configure your enviornment
* `echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env`
* `echo "sendgrid.env" >> .gitignore`
* `source ./sendgrid.env`

