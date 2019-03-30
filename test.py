from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC1be5c12bbc465a99586baa2b766fc195'
auth_token = '756d2723cc1ff6dd08351f12f411326f'
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages \
        .create(
        body="Parkinson on Move!",
        from_='+18327261605',
        to='+918851465800'
    )
    print(message.sid)