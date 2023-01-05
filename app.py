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
import csv
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
    def showDistro(distro):
        

        with open('Distro_link.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
          
            for row in csv_reader:
                if row:
                    if row[0].lower()==distro:
                        return row[1]
            return False

    def register(num,str):
        # if checkname(num)==False:
        #     return False
        # else:
        flag=0
        name=""
        post=""
        for i in str:
            if i==':':
                flag=1
            elif flag==1:
                post+=i
            else:
                name+=i
        with open('numbers.txt', mode='a') as numbers_file:
            number_writer = csv.writer(numbers_file, delimiter=',')
            number_writer.writerow([num,name])
        with open('posts.txt', mode='a') as posts_file:
            post_writer = csv.writer(posts_file, delimiter=',')
            post_writer.writerow([name,post])
        return True

    def checkpost(name):
        with open('posts.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
          
            for row in csv_reader:
                if row:
                    if row[0]==name:
                        return row[1]
    def checkname(num):
        
        with open('numbers.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
          
            for row in csv_reader:
                if row:
                   if row[0]==num:
                        return row[1]
        return False;


    
    num=request.values.get('From')
    temp=checkname(num)
    usermsg=request.values.get('Body','')
    user_msg=request.values.get('Body','').lower()
    print(f"User message:{user_msg}")
    bot_resp=MessagingResponse()
    msg=bot_resp.message()
    if ':' in user_msg:
        if temp!=False:
            msg.body("You are already Registered!!\nContact admin for changes😉")
        else:
            register(num,usermsg)
            msg.body("Congratulations !! You are registered🎊")
    elif temp==False:
        msg.body("Register Yourself First by Sending\n<name>:<post>")
    else:
        if 'hello ' in user_msg or 'hi ' in user_msg or 'hey ' in user_msg or 'namaskar ' in user_msg or 'hola ' in user_msg or 'hello'==user_msg or 'hi'==user_msg or 'hey'==user_msg or 'namaskar'==user_msg or 'hola'==user_msg :
            pist=checkpost(temp)
            msg.body(f"Hello {temp}, I am a Bot created for Walchand Linux users Group 🐧!!\n\nI Welcome you {pist} 😁!! \n\n What can i help you with? 🙇‍♂️\n\n Type show to see available Commands")
        elif 'main board' in user_msg or '1' in user_msg:
            p=open("mainBoard.txt",'r')
            p=p.read()
            msg.body(p)
                #msg.body("President:\nDnyaneshwari Kolapkar\nVice President:\nKrishnacharan Bhola\n\nfor more visit www.wcewlug.org")
        elif 'show' in user_msg or '9' in user_msg:
            msg.body("1.List of Main Board\n2.List of Assistant Board\n3.Register for ongoing event\n4.Linux quote\n5.WLUG Logo\n6.User Info\n7. Distro Link for Download \n8.Show all Distros\n9. Show Commands")
        elif 'logo' in user_msg or '5' in user_msg:
            msg.media("https://www.wcewlug.org/images/wluglogo.png")
        elif 'user' in user_msg or '6' in user_msg or "info" in user_msg:
            pist=checkpost(temp)
            msg.body(f"Name:{temp}\nPost:{pist}")
        elif 'register event' in user_msg or '3' in user_msg or 'event' in user_msg:
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
            p=open("asstBoard.txt",'r')
            p=p.read()
            msg.body(p)
        elif 'distro' in user_msg or '7' in user_msg:
            msg.body("To get downloading link for any Linux Distro, type:\n<Distro name>=?")
        elif '=?' in user_msg or '?' in user_msg :
            distro=""
            for i in user_msg:
                if i=='=' or i==' ':
                    break
                distro+=i
            link=showDistro(distro)
            if(link):
                msg.body(f"Here's your Download link for {distro}✌\n\n {link}")
            else:
                msg.body(f"Sorry! We couldn't find the {distro} link😔")
        elif 'all' in user_msg or '8' in user_msg:
            p=open("Alldistro.txt",'r')
            p=p.read()
            msg.body(f"Here is a list of all available Distros🐧:\n\n{p}")
        else: 
            msg.body("Sorry,Didn't get What you said! Send a Valid Command")
    print(f"Replied message:"+str(bot_resp))
    return str(bot_resp) 

if __name__ == "__main__":
    app.run(debug=True)
