# PiCam
A python3 file that controls a Raspberry Pi camera, LEDs, and motion sensor.

# Prerequisites to run script
* `sudo apt-get update`
* `sudo apt-get install python3-picamera`

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