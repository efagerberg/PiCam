import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("SpyPi@no-reply")
subject = "Motion Detected"
to_email = Email("sendToUser@example.com")
content = Content("text/plain", "We have detected motion from your pi!\n\n")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)