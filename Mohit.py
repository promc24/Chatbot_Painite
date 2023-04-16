ans_choices = ["1", "2", "3", "4", "5"]

qs = ["1. How much do your obsessive thoughts interfere with functioning in your social, work, or other roles? \n"
          " 1 being None \n 2 being Slight interference, but no impairment \n 3 being Definite interference, but managable \n"
          " 4 being Substantial intereference \n 5 being Extreme intereference, incapacitating \n "
          " 1 being None \n 2 being less than 1 hour per day \n 3 being 1-3 hours \n "
          "4 being 3-8 hours \n 5 being more than 8 hours a day.", 
      "2. How much do your obsessive thoughts interfere with functioning in your social, work, or other roles? \n"
          " 1 being None \n 2 being Slight interference, but no impairment \n 3 being Definite interference, but managable \n"
          " 4 being Substantial intereference \n 5 being Extreme intereference, incapacitating \n",
      "3. How much distress do your obsessive thoughts cause you? \n 1 being None \n 2 being Mild, not too disturbing \n "
           "3 being Moderate, disturbing, but still manageable \n 4 being Severe, very disturbing \n 5 being Extreme, near constant and disabling distress \n",
      "4. How much of an effort do you make to resist the obsessive thoughts? \n 1 being Always make an effort to resist, or don’t even need to resist \n"
          " 2 being Try to resist most of the time \n 3 being Make some effort to resist \n 4 being Reluctantly yield to all obsessive thoughts \n"
          " 5 being Completely and willingly yield to all obsessions \n",
      "5. How much control do you have over your obsessive thoughts? \n "
           "1 being Complete control \n 2 being Much control, usually able to stop or divert obsessions with some effort and concentration \n 3 being Moderate control, sometimes able to stop or divert obsessions \n "
          " 4 being Little control, rarely successful in stopping or dismissing obsessions \n 5 being No control, rarely able to even momentarily alter obsessive thinking \n",
      "6. How much time do you spend performing compulsive behaviors? \n "
           "1 being None \n 2 being less than 1 hour per day \n 3 being 1-3 hours \n "
          "4 being 3-8 hours \n 5 being more than 8 hours a day. \n",
      "7. How much do your compulsive behaviors interfere with functioning in your social, work, or other roles? \n"
          " 1 being None \n 2 being Slight interference, but no impairment \n 3 being Definite interference, but managable \n"
          " 4 being Substantial intereference \n 5 being Extreme intereference, incapacitating \n",
      "8. How anxious would you become if you were prevented from performing your compulsive behaviors? \n"
          " 1 being No anxiety \n 2 being Only slightly anxious \n 3 being Some anxiety, but managable \n"
          " 4 being Prominent and disturbing anxiety \n 5 being Extreme, incapacitating anxiety \n",
      "9. How much of an effort do you make to resist the compulsions? \n 1 being Always make an effort to resist, or don’t even need to resist \n"
          " 2 being Try to resist most of the time \n 3 being Make some effort to resist \n 4 being Reluctantly yield to all compulsions \n"
          " 5 being Completely and willingly yield to all compulsions \n",
      "10. How much control do you have over your compulsive thoughts? \n "
           "1 being Complete control \n 2 being Much control, usually able to stop or divert compulsive behavior with some effort and concentration \n 3 being Moderate control, sometimes able to stop or divert compulsive behavior \n "
          " 4 being Little control, rarely successful in stopping or dismissing compulsive behavior \n 5 being No control, rarely able to even momentarily alter compulsive behavior \n"]

def OCD():
    tot = 0
    print('''
    You are about to take the Yale-Brown Obsessive Compulsive test, 
    which will collect the scores of your answers to assess the severity and different symptoms in people with OCD. 
    Take a look at the definitions of obessions and compulsions below to help you understand it better: 

    'Obsessions are unwelcome or distressing ideas, thoughts, images or impulses that repeatedly enter your mind.
    They may seem to occur against your will. They may be repugnant to you, are often senseless, 
    and may not fit your actual personality at all (for example, the recurrent thought or impulse to harm to your children, even though you never would).'

    'Compulsions are behaviors or acts that you feel driven to perform, even though you may recognize them as senseless or excessive. 
    At times, you may try to resist doing them, but this may prove difficult. You may experience anxiety that does not diminish until the behavior is completed.'

    Please answer the questions based on the average occurence of each behaviour over the past week. 
    Please answer by writing in the corresponding number to your desired answer.  
    Please answer honestly and take your time. 
    ''')
    for ques in qs:
        print(qs)
        ans = input("Your answer: ")
        if ans in ans_choices:
            tot = tot + int(ans)
        else:
            print("I am sorry, I didn't catch that. ")
            error_ans = input("Would you like to try the test again? ")
            if error_ans == "yes" or "Yes" or "ok" or "Ok" or "Okay" or "sure" or "Sure" or "yeah" or "Yeah":
                OCD()
            else:
                print("Okay, no worries! /nThanks for trying! /nI am always here to help! ")
                break
        if tot <= 8: 
            print("You scored " + str(tot) + ", which shows you have few or no OCD symptoms. I wouldn'y worry if I was you! However if you'd like to speak to someone, I can help with that. ")
        elif tot >= 9 and final < 20:
            print("You scored " + str(tot) + ", which shows you have mild OCD symptoms. You show a few symptoms, although not many to cause concern. However if you'd like to speak to someone, I can help with that. ")
        elif tot >= 20 and final < 30:
            print("You scored " + str(tot) + ", which shows you have moderate OCD symptoms. It is best to speak to someone to prevent it from controlling you. I can help in finding a professional to speak with, if you'd like. ")
        elif tot >= 30 and final < 40:
            print("You scored " + str(tot) + ", which shows you have severe OCD symptoms. It is recommended to speak to a professional therapist to prevent OCD from overcoming you. I can help with that if you'd like. ")
        elif tot >= 40 and final < 51:
            print("You scored " + str(tot) + ", which shows you have extreme OCD symptoms. It is highly advisable that you speak with a professional therapist as soon as possible. I can help with that, if you'd like. ")
