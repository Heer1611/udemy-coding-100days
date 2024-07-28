import os
from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        try:
            message = self.client.messages.create(
                from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
                body=message_body,
                to=os.environ["TWILIO_VERIFIED_NUMBER"]
            )
            print(f"SMS sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")

    def send_whatsapp(self, message_body):
        try:
            message = self.client.messages.create(
                from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
                body=message_body,
                to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
            )
            print(f"WhatsApp message sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send WhatsApp message: {e}")

# Usage example
if __name__ == "__main__":
    nm = NotificationManager()
    nm.send_whatsapp("Test message")
