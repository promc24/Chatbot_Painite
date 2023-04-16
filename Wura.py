ans_choices=["0","1"]
questions=[
                "you felt so good or so hyper that other people thought you were not your normal self or you were so hyper that you got into trouble?",
                "you were so irritable that you shouted at people or started fights or arguments?", "you felt much more self-confident than usual?",
                "you got much less sleep than usual and found that you didn’t really miss it?", "you were more talkative or spoke much faster than usual?",
                "thoughts raced through your head or you couldn’t slow your mind down?",
                "you were so easily distracted by things around you that you had trouble concentrating or staying on track?",
                "you had more energy than usual?","you were much more active or did many more things than usual?",
                "you were much more social or outgoing than usual, for example, you telephoned friends in the middle of the night?",
                "you were much more interested in sex than usual",
                "you did things that were unusual for you or that other people might have thought were excessive foolish or risky?",
                "spending money got you or your family in trouble?"]



def biPolar():
  total_yes=0
  print("Painite is using the Mood Disorder Questionnaire (MDQ).")
  print ("The MDQ was developed by a team of psychiatrists, researchers and consumer advocates to address a critical need for timely and accurate diagnosis of bipolar disorder.")
  for question in questions:
    print ("has there been a period of time where you didnt feel like yourself and...")
    print(question)
    ans=input("input answer using 1 for yes and 0 for no:")
    if ans in ans_choices :
            total_yes=total_yes+int(ans)
    else:
      print("Sorry, can you please answer with the given numbers?")
      ans = input("Would you like to retry the test?")
      if ans=="yes" or ans=="ok" or ans=="Yes" or ans=="Ok" or ans=="YES" or ans=="OK" :
        biPolar()
        break
      else:
        print("I understand that you made an effort.\nPlease know that you are more than welcome to retake the quiz when you feel like it.\nI am always here, ready to help!\n Have a nice day")
        break     
     
  if total_yes<7:
    print("Good news.Your score is: "+str(total_yes)+ ". You have a negative screen.")
  
  elif total_yes>=7:
    print("Your score is: "+str(total_yes)+ ". You have a positive screen. According to the test a positive screen should be followed by a comprehensive medical evaluation for Bipolar Spectrum Disorder.")
  print("This scale is not designed to make a diagnosis of anxiety or take the place of a professional diagnosis. \n If you suspect that you suffer from PTSD, please consult a mental health professional as soon as possible.")
  print("Take care and goodbye.")

if __name__ == "__main__":
     biPolar()
     

    
    

  
  
  
  

                
                
