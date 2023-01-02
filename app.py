# from flask import Flask, request
# import requests
# from twilio.twiml.messaging_response import MessagingResponse

# app=Flask(__name__)

# @app.route("/")
# def hello():
#     return "hello worlld"

# # def sms_reply():
# #     msg=request.form.get('Body')
# #     resp=MessagingResponse()
# #     resp.message("You Said:{}".format(msg))
# #     return str(resp)
# @app.route("/bot",methods=['POST'])
# def bot():
#     user_msg=request.values.get('Body','').lower()
#     bot_resp=MessagingResponse()
#     msg=bot_resp.message()
#     if 'hello' in user_msg or 'hi' in user_msg or 'hey' in user_msg:
#         msg.body("Hello There, I am a Bot created for Walchand Linux users Group 🐧!!\n What can i help you with?")
#     elif 'main board' in user_msg:
#         msg.body("President:Dnyaneshwari Kolapkar\nVice President:Krishnacharan Bhola\n\nfor more visit www.wcewlug.org")
#     elif 'show' in user_msg:
#         msg.body("1.List of Main Board\n2.List of Assistant Board\n3.Register for ongoing event\n4.Linux Fact")
#     elif 'logo' in user_msg:
#         msg.media("https://www.wcewlug.org/images/wluglogo.png")
#     elif 'quote' in user_msg:
#         r=requests.get('https://api.quotable.io/random')
#         if r.status_code==200:
#             data=r.json()
#             quote=f'{data["content"]} ({data["author"]})'
#         else:
#             quote='I could not retrieve a quote, Sorry!'
#         msg.body(quote)
#     else: 
#         msg.body('Sorry , Didnt get What you said! Send a Valid Command')
#     return str(bot_resp) 

# if __name__=='main_':
#     app.run(debug=True)

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    # msg = request.form.get('Body')

    # # Create reply
    # resp = MessagingResponse()
    # resp.message("You said: {}".format(msg))

    # return str(resp)
    user_msg=request.values.get('Body','').lower()
    bot_resp=MessagingResponse()
    msg=bot_resp.message()
    if 'hello' in user_msg or 'hi' in user_msg or 'hey' in user_msg:
        msg.body("Hello There, I am a Bot created for Walchand Linux users Group 🐧!!\n What can i help you with?\n\n Type show to see available Commands")
    elif 'main board' in user_msg or '1' in user_msg:
        msg.body("President:\nDnyaneshwari Kolapkar\nVice President:\nKrishnacharan Bhola\n\nfor more visit www.wcewlug.org")
    elif 'show' in user_msg or '6' in user_msg:
        msg.body("1.List of Main Board\n2.List of Assistant Board\n3.Register for ongoing event\n4.Linux quote\n5.WLUG Logo\n6.Show Commands")
    elif 'logo' in user_msg or '5' in user_msg:
        msg.media("https://www.wcewlug.org/images/wluglogo.png")
    elif 'register' in user_msg or '3' in user_msg:
        msg.body("No ongoing events from WLUG")
    elif 'quote' in user_msg or '4' in user_msg:
        r=requests.get('https://api.quotable.io/random')
        if r.status_code==200:
            data=r.json()
            quote=f'{data["content"]} ({data["author"]})'
        else:
            quote='I could not retrieve a quote, Sorry!'
        msg.body(quote)
    elif 'assistant board' in user_msg or '2' in user_msg:
        msg.body("Assistant Technical Advisor:\n Aradhya Pitlawar")
    else: 
        msg.body('Sorry , Didnt get What you said! Send a Valid Command')
    return str(bot_resp) 

if __name__ == "__main__":
    app.run(debug=True)
