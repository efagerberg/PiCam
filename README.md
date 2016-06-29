# PiCam
A python3 file that controls a Raspberry Pi camera, LEDs, and motion sensor.

# Install MotionEye
* Refer to `https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian`
* `./install.sh`
* Add init script with
   cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
   systemctl daemon-reload
   systemctl enable motioneye
   systemctl start motioneye

# Update motioneye
* ./upgrade.sh

# Configure Sendgrid
Make an account and generate a free API Key
https://sendgrid.com/free/?source=sendgrid-python

Configure your enviornment
* `echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env`
* `echo "sendgrid.env" >> .gitignore`
* `source ./sendgrid.env`

Install sendgrid
* `sudo pip install sendgrid`

Change the to_email value in "send_email.py" to send the email to yourself for testing purposes.
