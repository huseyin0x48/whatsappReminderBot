from twilio.rest import Client
account_sid = 'AC4d9fc1a30b341bd5e52523ab4938af82' # Add your Twilio Account's SID
auth_token = '8de296e1801f57b5c7443aa6e0d254b8' # Add your Twilio Account's Auth Token
client = Client(account_sid, auth_token)
def send_rem(date,rem):
  message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='*REMINDER* '+date+'\n'+rem,
  to='whatsapp:+905070657355' # Add your WhatsApp No. here
)
print(message.sid)