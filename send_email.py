import base64
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, Email, Content


if __name__ == "__main__":
    sg = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    print os.environ.get('SENDGRID_API_KEY')
    from_email = Email("SpyPi@no-reply")
    subject = "Motion Detected"
    to_email = Email("adioevan@gmail.com")
    content = Content("text/plain", "Test!\n\n")
    mail = Mail(from_email, subject, to_email, content)

    for i in range(2):
        with open("test.jpg", "rb") as jpg_file:
            attachment = Attachment()
            attachment.set_filename("ducky-{}.jpg".format(i))
            attachment.set_content(base64.b64encode(jpg_file.read()))
            attachment.set_type('image/jpg')
            mail.add_attachment(attachment)

    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
