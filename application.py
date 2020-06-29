from flask import Flask,make_response, jsonify,request
from flask_cors import CORS
from result_lookup import Results
from send_sms import SendSms
import os
app = Flask(__name__)
CORS(app,expose_headers=["Content-Disposition"])
@app.route('/')
def root():
    CallSid=request.args.get('CallSid')
    CallFrom=request.args.get('CallFrom')
    CallTo=request.args.get('CallTo')
    CallType=request.args.get('CallType')
    From=request.args.get('From')
    To=request.args.get('To')
    result = Results()
    marks = result.getResult(CallFrom)
    msg = ' CallFrom:'+str(CallFrom)+' Result:'+str(marks)
    print(msg)
    send_sms = SendSms()
    data = send_sms.send_my_sms(msg,CallFrom)
    print(msg)
    return make_response(data,200)

if __name__ =='__main__':
    #application = Application()
    #application.run()
    port= int(os.getenv('PORT',8080))
    app.run(port=port, host="0.0.0.0",debug=True)


