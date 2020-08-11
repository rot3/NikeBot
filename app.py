from flask import Flask, request, redirect,Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse()
    body = request.form['Body']

    with open('verify.text','w+') as file:
        file.write(body)

    resp.message("The Robots are coming! Head for the hills!{}".format(body))
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# app = Flask(__name__)
# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()
#     body = request.form['Body']
#     verification_code = body
#     # Add a message
#     #resp.message("The Robots are coming! Head for the hills!{}".format(body))
    
#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)