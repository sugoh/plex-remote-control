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
    body='Hipster-Netflicks Plex Server successfully restarted. REPLY WITH 0 to shut down. Otherwise, have a wonderful day.',
    from_='TWILIO_PHONE_NUMBER',
    to='YOUR_MOBILE_NUMBER')

print(message.sid)
