import sendgrid
from sendgrid.helpers.mail import Mail
from app import app

def send_email(to_email, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=app.config['SENDGRID_API_KEY'])
    email = Mail(
        from_email='from@example.com',
        to_emails=to_email,
        subject=subject,
        plain_text_content=content)
    response = sg.send(email)
    return response.status_code
