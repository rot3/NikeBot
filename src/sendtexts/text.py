from twilio.rest import Client
from credentials import auth_tok, account_num, numbers

def send_text(message, reciever = numbers["me"]):
    
    client = Client(account_num,auth_tok)
    client.messages.create(
        to= reciever, 
        from_=twilio_num,
        body=message) 