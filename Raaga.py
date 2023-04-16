'''Chatbot Code'''
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
  r2=r.capitalize()
  if r=='Birmingham' or r=='birmingham':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='London' or r=='london':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Manchester'or r=='manchester':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Bradford'or r=='bradford':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Leeds'or r=='leeds':
    h=hospitals(r2)
    s=support_groups(r2)
  for i in range(0,len(h)):
    strh=strh+"\n"+str(h[i])
    strh.strip('()')
  for j in range(0,len(s)):
    strs=strs+"\n"+str(s[j])
    strs.strip('()')
  return(strh+"\n"+strs)



def details2():
  r=fileread("getcityname.txt")
  strh=""
  strs=""
  r2=r.capitalize()
  if r=='Birmingham' or r=='birmingham':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='London' or r=='london':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Manchester'or r=='manchester':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Bradford'or r=='bradford':
    h=hospitals(r2)
    s=support_groups(r2)
  elif r=='Leeds'or r=='leeds':
    h=hospitals(r2)
    s=support_groups(r2)
  for i in range(0,len(h)):
    strh=strh+"\n"+str(h[i])
    strh.strip('()')
  for j in range(0,len(s)):
    strs=strs+"\n"+str(s[j])
    strs.strip('()')
  return(strh+"\n"+strs)




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
    elif r=="Depression" or r=="depression" or r=="1":
        return("Please access the test by the link\nhttps://painite.neocities.org/Depression.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="Anxiety" or r=="anxiety" or r=="2":
        return("Please access the test by the link\nhttps://painite.neocities.org/anxiety.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="PTSD" or r=="ptsd" or r=="3":
        return("Please access the test by the link\nhttps://painite.neocities.org/ptsd.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="Schizophrenia" or r=="schizophrenia" or r=="4":
        return("Please access the test by the link\nhttps://painite.neocities.org/schizophrenia.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="OCD" or r=="ocd" or r=="5":
        return("Please access the test by the link\nhttps://painite.neocities.org/ocd.html\n After taking the test, if you wish to see hospitals available in your city, then please enter your city name:")
    elif r=="Bipolar" or r=="bipolar" or r=="6":
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


 
 '''HTML code for HOME page'''
 
 <!DOCTYPE html>
<html>
    <head>
        <title>Self-Assessment</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
            <meta name="viewport" content="width=device-width, initial-scale=1">
                <style type="text/css">
                    ul {
                        li: right;
                    }
                
                .navbar-default .navbar-nav > li > a {
                    color: black;
                    font-weight: bold;
                    margin: 0;
                }
                
                .navbar-header > a {
                    color: black;
                    font-weight: bold;
                }
                
                .navbar {
                    margin:0;
                }
                
                .row {
                    padding-top: 2vh;
                    padding-bottom: 2vh;
                }
                .illness {
                    border-radius: 10px;
                    margin: auto;
                    padding: 3vh;
                    background: #ECF0F1;
                }
                
                #screening-button {
                    margin: 4vh auto 2vh auto;
                    padding: 2vh;
                    background-color: #2196F3;
                    text-align: center;
                    color: white;
                    display: block;
                    width: 20vw;
                    opacity: 0.9;
                    border: none;
                }
                
                
                #screening-button:hover {
                    opacity:1;
                }
                
                @media screen and (max-width: 700px) {
                    #screening-button {
                        width: 50vw;
                    }
                    
                    .col-sm-6 {
                        padding-top: 4vh;
                        padding-bottom: 4vh;
                    }
                }
                </style>
    </head>
    <body>
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Painite</a>
                    <img src="/logo.png" ALIGN="justify"/>
                    <img src="/icon.png" ALIGN="left" />
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="https://painite.neocities.org/Home.html">Home</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <div class="container">
            <h1 style="text-align: center;">Self-Assessment</h1>
            <div class = "row">
                <div class = "col-sm-6" id = "depression">
                    <div class = "illness">
                        <h3 style="text-align: center;">Depression</h3>
                        <a href="https://painite.neocities.org/Depression.html" class="btn btn-info" role="button" id = "screening-button">Take a Screening</a>
                    </div>
                </div>
                <div class = "col-sm-6" id = "anxiety">
                    <div class = "illness">
                        <h3 style="text-align: center;">Generalized Anxiety Disorder</h3>
                        <a href="https://painite.neocities.org/anxiety.html" class="btn btn-info" role="button" id = "screening-button">Take a Screening</a>
                    </div>
                </div>
            </div>
            
            <div class = "row">
                <div class = "col-sm-6" id = "bipolar">
                    <div class = "illness">
                        <h3 style="text-align: center;">Bipolar Disorder</h3>
                        <a href="https://painite.neocities.org/bipolar.html" class="btn btn-info" role="button" id = "screening-button">Take a Screening</a>
                    </div>
                </div>
                <div class = "col-sm-6" id = "ocd">
                    <div class = "illness">
                        <h3 style="text-align: center;">Obsessive Compulsive Disorder</h3>
                        <a href="https://painite.neocities.org/ocd.html" class="btn btn-info" role="button" id = "screening-button">Take a Screening</a>
                    </div>
                </div>
            </div>
            
            <div class = "row">
                <div class = "col-sm-6" id = "schizophrenia">
                    <div class = "illness">
                        <h3 style="text-align: center;">Schizophrenia</h3>
                        <a href="https://painite.neocities.org/schizophrenia.html" class="btn btn-info" role="button" id = "screening-button">Take a Screening</a>
                    </div>
                </div>
                <div class = "col-sm-6" id = "ptsd">
                    <div class = "illness">
                        <h3 style="text-align: center;">Post-Traumatic Stress Disorder</h3>
                        <a href="https://painite.neocities.org/ptsd.html" class="btn btn-info" role="button" id = "screening-button">Take a Screening</a>
                    </div>
                </div>
            </div>
          </body>
</html>
 
 '''HTML CODE for depression'''
 
 <!DOCTYPE html>
<html>
<head>
<title>Self-assessment</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
    ul {
        li: right;
    }

    .navbar-default .navbar-nav > li > a {
        color: black;
        font-weight: bold;
        margin: 0;
    }

    .navbar-header > a {
        color: black;
        font-weight: bold;
    }

    .navbar {
        margin:0;
    }

    .myRadio {
    display: block;
    position: relative;
    cursor: pointer;
    padding-left: 5vh;
    margin: 2vh;
    font-weight: normal;
    }

    .myRadio input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    }

    .checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 20px;
    width: 20px;
    background-color: #eee;
    border-radius: 50%;
    }

    .myRadio:hover input ~ .checkmark {
    background-color: #ccc;
    }

    .myRadio input:checked ~ .checkmark {
    background-color: #2196F3;
    }

    .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }

    .myRadio input:checked ~ .checkmark:after {
        display: block;
    }

    .question {
        font-weight: bold;
        background: #ECF0F1;
        padding: 2vh;
    }

    #submit-button {
        margin: 4vh auto 2vh auto;
        padding: 2vh;
        background-color: #2196F3;
        text-align: center;
        color: white;
        display: block;
        width: 20vw;
        opacity: 0.9;
        border: none;
    }


    #submit-button:hover {
          opacity:1;
        }

    #result {
      display: none;
      background: #ECF0F1;
      padding: 3vh;
      border-radius: 10px;

    }

    #consult-button {
        margin: 4vh auto 2vh auto;
        padding: 2vh;
        background-color: #2196F3;
        text-align: center;
        color: white;
        display: block;
        width: 20vw;
        opacity: 0.9;
        border: none;
    }


    #consult-button:hover {
          opacity:1;
        }

    @media screen and (max-width: 700px) {
      #consult-button {
          width: 50vw;
      }
    }
</style>
</head>
<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span> 
                </button>
                <a class="navbar-brand" href="#">PAINITE</a>
                <img src="/logo.png" ALIGN="justify"/>
                <img src="/icon.png" ALIGN="left" />
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav navbar-right">
                    <li class="active"><a href="https://painite.neocities.org/Home.html">Home</a></li>
            </div>
        </div>
    </nav>

    <div class = "container">
        <h1 style="text-align: center;">Self-Assessment for Depression</h1>
        <p style="text-align: justify;"> Painite uses the Goldberg Depression Questionnaire. All rights reserved to Ivan Goldberg (1993). Adopted from the printed edition of the Goldberg Depression Inventory for electronic distribution.</p>        
        <section id = "test" style="padding-top: 3vh">
        <p>During the last week, how often have you been bothered by the following problems?</p>
            <div id = "q1">
                <p class = "question">1. I do everything slowly.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q1">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q1">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q1">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q1">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q1">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q1">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q2">
                <p class = "question">2. My future seems hopeless.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q2">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q2">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q2">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q2">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q2">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q2">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q3">
                <p class = "question">3. I find it hard to concentrate when I read.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q3">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q3">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q3">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q3">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q3">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q3">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q4">
                <p class = "question">4. All joy and pleasure seem to have disappeared from my life.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q4">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q4">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q4">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q4">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q4">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q4">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q5">
                <p class = "question">5. I find it hard to make decisions.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q5">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q5">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q5">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q5">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q5">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q5">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q6">
                <p class = "question">6. I have lost interest in things that used to mean a lot to me.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q6">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q6">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q6">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q6">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q6">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q6">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q7">
                <p class = "question">7. I feel sad, depressed and unhappy.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q7">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q7">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q7">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q7">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q7">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q7">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q8">
                <p class = "question">8. I feel restless and cannot relax.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q8">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q8">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q8">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q8">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q8">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q8">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q9">
                <p class = "question">9. I feel tired.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q9">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q9">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q9">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q9">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q9">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q9">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q10">
                <p class = "question">10. I find it hard to do even trivial things.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q10">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q10">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q10">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q10">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q10">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q10">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q11">
                <p class = "question">11. I feel guilty and deserve to be punished.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q11">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q11">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q11">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q11">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q11">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q11">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q12">
                <p class = "question">12. I feel like a failure.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q12">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q12">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q12">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q12">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q12">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q12">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q13">
                <p class = "question">13. I feel empty - more dead than alive.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q13">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q13">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q13">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q13">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q13">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q13">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q14">
                <p class = "question">14. My sleep is disturbed: too little, too much or disturbed sleep.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q14">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q14">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q14">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q14">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q14">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q14">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q15">
                <p class = "question">15. I wonder HOW I could commit suicide.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q15">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q15">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q15">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q15">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q15">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q15">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q16">
                <p class = "question">16. I feel confined and imprisoned.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0"  name="q16">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q16">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q16">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q16">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q16">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q16">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q17">
                <p class = "question">17. I feel down even when something good happens to me.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q17">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q17">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q17">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q17">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q17">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q17">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div id = "q18">
                <p class = "question">18. I have lost or gained weight without being on a diet.</p>
                <label class = "myRadio">Not at all
                  <input type="radio" value = "0" name="q18">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Only slightly
                  <input type="radio" value = "1" name="q18">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Partly
                  <input type="radio" value = "2" name="q18">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">Quite a lot
                  <input type="radio" value = "3" name="q18">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">A lot
                  <input type="radio" value = "4" name="q18">
                  <span class="checkmark"></span>
                </label>
                <label class = "myRadio">To a great extent
                  <input type="radio" value = "5" name="q18">
                  <span class="checkmark"></span>
                </label>
            </div>

            <div>
              <input type = "submit" value = "Submit" id = "submit-button" onclick = "calculate()">
            </div>
        </section>

        <section id = "result">
          <h3 id = "result-type" style="text-align: center;"></h3>
          <p style="text-align: justify;">Please be noted that this questionnaire can be used to show your doctor how your symptoms have changed from one visit to the next.  Changes of five or more points are significant. This scale is not designed to make a diagnosis of depression or take the place of a professional diagnosis.  If you suspect that you are depressed, please consult a mental health professional as soon as possible.</p>
          <div>
              <input type = "button" value = "Consult a psychiatrist" id = "consult-button">
          </div>
        </section>
        
        <script type="text/javascript">
            function calculate()
            {
              var ans_array = [];
              var i = 1;
              var ans = 0;
              var count=0;
              for(i = 1; i <= 18; i++)
              {
                var q = document.getElementsByName("q"+i.toString());
                var j = 0;
                var temp=0;
                for(j = 0; j < 6; j++)
                {
                    if(q[j].checked)
                    {
                      count++;
                      ans_array[i-1] = q[j].value;
                      ans += parseInt(q[j].value);
                    }
                    
                }
                
              }
              if(count!=18)
              {
                alert("Please make a selection.");
                return false;
              }
              
              console.log(ans);

              // var modalresult = document.getElementById("resultModal");
              // modalresult.style.display = "block";
              // document.getElementsByTagName("body")[0].style.background = "blue";

              var diag;

              if(ans <= 9) diag = "Depression unlikely"
              else if(ans <= 21) diag = "Possible symptoms that may be due to depression or other medical issues"
              else if(ans<= 35)  diag = "Mild to Moderate Depression"
              else if(ans <= 53) diag = "Moderate to Severe Depression"
              else if (ans > 54)  diag = "Severely Depressed"

              document.getElementById("test").style.display = "none";
              document.getElementById("result-type").innerHTML = diag;
              document.getElementById("result").style.display = "block";

              return true;

            }

        </script>
    </div>
</body>
</html>

    ''' Depression Test  NOT USED'''
    def DepressionTest():
    print(" Painite uses the Goldberg Depression Questionnaire")
    print("All rights reserved to 1993 Ivan Goldberg. \n Adopted from the printed edition of the Goldberg Depression Inventory for electronic distribution. ")
    print("During the last week, how often have you been bothered by the following problems?")
    print("Please answer with the following numbers:")
    print("0 = Not at all ")
    print("1 = Just a little")
    print("2 = Somewhat")
    print("3 = Moderately")
    print("4 = Quite a lot")
    print("5 = Very much")

    questions = ["1) I do things slowly", 
             "2) My future seems hopeless",
             "3) It is hard for me to concentrate on reading", 
             "4) The pleasure and joy has gone out of my life", 
             "5) I have difficulty making decisions",
             "6) I have lost interest in aspects of life that used to be important to me",
             "7) I feel sad, blue, and unhappy",
             "8) I am agitated and keep moving around",
             "9) I feel fatigued",
             "10) It takes great effort for me to do simple things",
             "11) I feel that I am a guilty person who deserves to be punished",
             "12) I feel like a failure",
             "13) I feel lifeless -- more dead than alive",
             "14) My sleep has been disturbed -- too little, too much, or broken sleep",
             "15) I spend time thinking about how I might kill myself",
             "16) I feel trapped or caught",
             "17) I feel depressed even when good things happen to me",
             "18) Without trying to diet, I have lost, or gained, weight"]

    ans_choices = ['0','1','2','3','4','5']
    tot = 0
    for question in questions:
        print(question)
        user_ans = input("0,1,2,3,4,or 5:")
        if user_ans in ans_choices:
            tot = tot+int(user_ans)
        else:
            print("Sorry, can you please answer with the given numbers?")
            ans = input("Would you like to retry the test?")
            if ans=="yes" or ans=="ok" or ans=="Yes" or ans=="Ok" or ans=="YES" or ans=="OK" :
                DepressionTest()
                break
            else:
                print("I understand that you made an effort, please comeback when you feel like you want to retake it. I am always here, ready to help!")
                break
   # print("Your result till now is:")            
    if tot<10:
        print("Not depression likely.")
    elif tot>=10 and tot<18:
        print("Possible symptoms that may be due to depression or other medical issues.")
    elif tot>=18 and tot<22:
        print("Borderline depression.")
    elif tot>=22 and tot<36:
        print("Mild to moderate depression.")
    elif tot>=36 and tot<54:
        print("Moderate to severe depression.")
    else:
        print("Severely depressed")
    print("Please be noted that this questionnaire can be used to show your doctor how your symptoms have changed from one visit to the next. \n Changes of five or more points are significant.\n This scale is not designed to make a diagnosis of depression or take the place of a professional diagnosis. \n If you suspect that you are depressed, please consult a mental health professional as soon as possible.")
if __name__ == "__main__":
    DepressionTest()
