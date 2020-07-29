from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect, send_from_directory
import requests
import gpt_2_simple as gpt2

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    resp = MessagingResponse()
    Prefix = request.values['Body']
    print("received: " + Prefix)
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    resp_str = str(gpt2.generate(sess,
                length=50,
                temperature=.8,
                prefix=Prefix,
                top_p=0.9,
                nsamples=1,
                return_as_list=True)[0])
    print("texting back: " + resp_str)
    resp.message(resp_str)
    return str(resp)