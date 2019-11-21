# Imports
import os
from twilio.rest import Client

# Authenticate client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
api_key = os.environ['TWILIO_API_KEY']
api_secret = os.environ['TWILIO_API_SECRET']
client = Client(api_key, api_secret, account_sid)

# Send message
message = client.messages.create(
    body='Your Plex Media Server is down. Now attempting to restart...',
    # Replace TWILIO_NUMBER with your Twilio account number
    from_='TWILIO_NUMBER',
    # Replace MOBILE_NUMBER with the phone number you're using to receive the notification
    to='MOBILE_NUMBER')

print(message.sid)
