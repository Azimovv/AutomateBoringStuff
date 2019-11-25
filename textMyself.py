# Script to send a text (to myself)

# Presets
accountSID = 'AC[REDACTED]'
authToken = '[REDACTED]'
myNumber = '+[REDACTED]'
twilioNumber = '+[REDACTED]'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)