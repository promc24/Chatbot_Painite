print("Painite is using the Schizophrenia Test and Early Psychosis Indicator")
print("The Schizophrenia Test and Early Psychosis Indicator (STEPI, Version 2011.1) for Prodromal Syndromes and Psychosis is designed as a simple screening quiz to help identify symptoms of the schizophrenia.")
print("For the past 6 months how has this medical condition bothered you?")
print("Can you please answer based on the following number range:")
print("0= Not at all")
print("1= Just a little")
print("2= Somewhat")
print("3= Moderately")
print("4= Quite a lot")
print("5= All the time")
quizes=["1)I believe that others control what I think and feel",
      "2) I hear or see things that others do not hear or see",
      "3)I feel it is very difficult for me to express myself in words that others can understand",
      "4)I feel I share absolutely nothing in common with others, including my friends and family",
      "5)I believe in more than one thing about reality and the world around me that nobody else seems to believe in",
      "6) Others don’t believe me when I tell them the things I see or hear,"
      "7)I can’t trust what I’m thinking because I don’t know if it’s real or not",
      "8)I have magical powers that nobody else has or can explain",
      "9)Others are plotting to get me",
      "10) I find it difficult to get a hold of my thoughts",
      "11) I am treated unfairly because others are jealous of my special abilities",
      "12)I talk to another person or other people inside my head that nobody else can hear",]
ans_choice=['0','1','2','3','4','5']
def SchizophreniaTest():
    tot=0
    for quiz in quizes:
        print (quiz)
        user_ans=input(ans_choice)
        if user_ans in ans_choice:
            tot=tot+int(user_ans)
        else:
            print("I dont't think you have schizophrenia")
    if tot<9:
        print("No schizophrenia")
    elif tot>=10 and tot<13:
        print("Possibility of early schizophrenia")
    elif tot>=14:
        print("Early schizophrenia")
    else:
        print("Serious schizophrenia")
SchizophreniaTest()
