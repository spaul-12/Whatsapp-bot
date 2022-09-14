from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world"


@app.route('/sms', methods=['POST'])
def sms():
    message = "Hello There"
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)


if __name__ == '__main__':
    app.run()




