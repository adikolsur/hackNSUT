from django.shortcuts import render
from twilio.rest import Client

account_sid = 'AC1be5c12bbc465a99586baa2b766fc195'
auth_token = '756d2723cc1ff6dd08351f12f411326f'
client = Client(account_sid, auth_token)

def index(req):
    return render(req, 'sms/index.html')

def send(req):
    message = client.messages \
        .create(
        body="Parkinson on Move!",
        from_='+18327261605',
        to='+918851465800'
    )
    print(message.sid)
    return render(req, 'sms/success.html')