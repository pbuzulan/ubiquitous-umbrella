# from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = 'your_twilio_account_sid'
AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms_notification(to_phone_number, message):
    # message = client.messages.create(
    #     body=message,
    #     from_=TWILIO_PHONE_NUMBER,
    #     to=to_phone_number
    # )
    return {"123"}
