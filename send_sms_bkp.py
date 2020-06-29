#Z26N1SVHHEL3CMGLFZTO1LAZQRR9ZVJM API Key
#W8XGKT0M20A5JTXI secret key
import requests
import json
class SMSSender():
 
  # get request
  def sendPostRequest(self, reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
    'apikey':apiKey,
    'secret':secretKey,
    'usetype':useType,
    'phone': phoneNo,
    'message':textMessage,
    'senderid':senderId
    }
    return requests.post(reqUrl, req_params)
    # myDict = {'text':'Hello from sendPostRequest'}
    # return myDict
if __name__ =='__main__': 
  URL = 'https://www.sms4india.com/api/v1/sendCampaign'
  smsSender = SMSSender()
  # get response
  response = smsSender.sendPostRequest(URL, 'Z26N1SVHHEL3CMGLFZTO1LAZQRR9ZVJM', 'W8XGKT0M20A5JTXI', 'stage', '8892472497', 'ABC123', 'Hello World' )
  """
  Note:-
  you must provide apikey, secretkey, usetype, mobile, senderid and message values and then requst to api
  """
  # print response if you want
  print(response.text)


