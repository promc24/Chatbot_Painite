#Python libraries that we need to import for our bot
from flask import Flask, request
from flask_mail import Mail, Message
from pymessenger.bot import Bot
import sqlite3 as sql


app = Flask(__name__)
ACCESS_TOKEN = 'EAAjZA2xibM0ABAOCaYxeA4odWqTGt6vYcxcaF7Ln8sZBuHLD5JrKQxTnPW4VY5MSO0B19qgAyyS0Wpd1NQgk33TYsY2ySZBa5cbZB5oX44d4Octfj1bvSlBK0NrSMJr5eqgMqLEzQ9JIEhP6tpBdxVWwW9zR8fkhUPZAoZANasVnn3EleZBCtg4'
VERIFY_TOKEN = 'COVENTRYJ4'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'



#to open and return file contents
def fileread(filename):
    f = open(filename, "r")
    textString = f.read()
    f.close()
    return textString

#to open and write into the file
def filewrite(filename,name):
  f=open(filename,"w")
  f.write(name)
  f.close()
  
#to recieve the message sent by user and return it
def getmessage():
    output = request.get_json()
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                return(message['message'].get('text'))
  
#Creating a database connection and returning hospital details
def hospitals(city_name):
  con = sql.connect('Chatbot.db')
  cur=con.cursor()
  cur.execute(''' SELECT City as "CITY:", Hospital as "Hospital Name:", Address as "ADDRESS:", Contact_no as "NUMBER:" FROM Hospitals WHERE City==?;''',(city_name,))
  for row in cur:
    return(row)
  con.close()

#Creating a database connection and returning support groups details
def support_groups(city_name):
  con = sql.connect('Chatbot.db')
  cur=con.cursor()
  cur.execute(''' SELECT City as "CITY:", Organisation  as "Name of the organisation:", Contact_no as "NUMBER:",Email as "EMAIL:", Address as "ADDRESS:" FROM Support_Groups WHERE City==?;''',(city_name,))
  for row in cur:
    return(row)
  con.close()
  
def details():
  n=getmessage()
  filewrite("getcityname.txt",n)
  r=fileread("getcityname.txt")
  strh=""
  strs=""
  r1=r.lower()
  r2=r1.capitalize()
  if r=='Birmingham' or r=='birmingham' or r=='BIRMINGHAM':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='London' or r=='london' or r=='LONDON':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Manchester'or r=='manchester' or r=='MANCHESTER':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Bradford'or r=='bradford' or r=='BRADFORD':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Leeds'or r=='leeds'or r=='LEEDS':
    h=hospitals(r2)
    s=support_groups(r2)
  for i in range(0,len(h)):
    strh=strh+"\n"+str(h[i])
    strh.strip('()')
  for j in range(0,len(s)):
    strs=strs+"\n"+str(s[j])
    strs.strip('()')
  return("HOSPITAL\n"+strh+"\n\nSUPPORT GROUP\n"+strs)



def details2():
  r=fileread("getcityname.txt")
  strh=""
  strs=""
  r1=r.lower()
  r2=r1.capitalize()
  if r=='Birmingham' or r=='birmingham' or r=='BIRMINGHAM':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='London' or r=='london' or r=='LONDON':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Manchester'or r=='manchester' or r=='MANCHESTER':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Bradford'or r=='bradford' or r=='BRADFORD':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Leeds'or r=='leeds'or r=='LEEDS':
    h=hospitals(r2)
    s=support_groups(r2)
  for i in range(0,len(h)):
    strh=strh+"\n"+str(h[i])
    strh.strip('()')
  for j in range(0,len(s)):
    strs=strs+"\n"+str(s[j])
    strs.strip('()')
  return("HOSPITAL\n"+strh+"\n\nSUPPORT GROUP\n"+strs)




#To send an automated mail
def send_mail():
  EMAIL_USER="painitehelp@gmail.com"
  EMAIL_PASSWORD="coventryj4"
  e=getmessage()
  filewrite("get_email.txt",e)
  r=fileread("get_email.txt")


  mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":EMAIL_USER,
    "MAIL_PASSWORD":EMAIL_PASSWORD
  }

  app.config.update(mail_settings)
  mail = Mail(app)
  with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[r,],
                      body=("Thanks for using Painite. The information you asked for is written below:\n"+str(details2())+"\n\nBest Regards, \nPainite\nhttps://painite.neocities.org/Home.html"))          
        if '@uni.coventry.ac.uk' in str(r) or '@gmail.com' in str(r) or '@yahoo.com' in str(r):     
          mail.send(msg)
          return(True)  
        else:
          return False
                      

#returns response to be sent, depending on the message recieved
def reply():
    r=getmessage()
    if r in fileread("Greeting.txt"):
        return("Hello, I am Painite. How may I help you?")
    elif r in fileread("Possible.txt"):
        return("That must be hard for you.\n Painite offers the following screening tests:\n 1.Depression\n 2.Anxiety\n 3.PTSD\n 4.Schizophrenia\n 5.OCD\n 6.Bipolar\n Would you like to take any of the screening tests?")
    elif r in fileread("positive.txt"):
        return("Which screening test do you want to try?")
    elif r in fileread("negative.txt"):
        return("I understand that you made an effort, and I respect your privacy. I am always here, ready to help!")
    elif r=="Depression" or r=="depression" or r=="1" or r=="DEPRESSION":
        return("Please access the test by the link\nhttps://painite.neocities.org/Depression.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="Anxiety" or r=="anxiety" or r=="2" or r=="ANXIETY":
        return("Please access the test by the link\nhttps://painite.neocities.org/anxiety.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="PTSD" or r=="ptsd" or r=="3" or r=="PTSD":
        return("Please access the test by the link\nhttps://painite.neocities.org/ptsd.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="Schizophrenia" or r=="schizophrenia" or r=="4" or r=="SCHIZOPHRENIA":
        return("Please access the test by the link\nhttps://painite.neocities.org/schizophrenia.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="OCD" or r=="ocd" or r=="5" or r=="Ocd":
        return("Please access the test by the link\nhttps://painite.neocities.org/ocd.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="Bipolar" or r=="bipolar" or r=="6" or r=="BIPOLAR":
        return("Please access the test by the link\nhttps://painite.neocities.org/bipolar.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif  r in fileread("allcities.txt"):
      if r in fileread("citynames.txt"):
        return (str(details())+"\n If u wish to get an email of the hospital details in you city please enter your email:")
    elif '@uni.coventry.ac.uk' in r or '@gmail.com' in r or '@yahoo.com' in r:
      a=send_mail()
      if a==True:
        return("Email has been sent. Please check your inbox.")
      elif a==False:
        return("Please enter a valid email")
    elif r in fileread("gratitude.txt"):
      return("Thank you for talking to painite. It was nice to talk to you. You can also access the other tests at https://painite.neocities.org/Home.html\nI hope you find the help you need.")
    else:
        return("I do not understand that. Can you please repeat that?")
        reply()
                    
                

#chooses a message to send to the user
def get_message():
    sample_responses = reply()
    # return selected item to the user
    return (sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


#Webhook port
if __name__ == "__main__":
               app.run(debug = True, host="0.0.0.0",port=8080)
