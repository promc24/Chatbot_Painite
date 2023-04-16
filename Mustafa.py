ans_choices=["0","1"]
questions= [
    "Have you ever felt you should cut down on your drinking?",
    "Have people annoyed you by criticising your drinking?",
    "Have you ever felt bad or guilty about your drinking?",
    "Have you ever had a drink first thing in the morning to steady your nerves or get rid of a hangover (eye-opener)?"]

def AlcoholDependence():
    print("Painite is using CAGE Questionnaire, A Screening Test for Alcohol Dependence.")
    print("With just 4 questions, this simple self-test has nonetheless proven accurate in identifying usage patterns that may reflect problems with alcohol. The test specifically focuses on the use of alcohol.")
    print("Please answer with the following numbers:")
    print("0 = No")
    print("1 = Yes ")
    tot = 0
    for question in questions:
        print(question)
        user_ans=input("answer choice:")
        if user_ans in ans_choices :
            tot=tot+int(user_ans)
        else:
            print("Sorry, can you please answer with the given numbers?")
            ans = input("Would you like to retry the test?")
            if ans=="yes" or ans=="ok" or ans=="Yes" or ans=="Ok" or ans=="YES" or ans=="OK" :
                AlcoholDependence()
                break
            else:
                print("I understand that you made an effort.\nPlease know that you are more than welcome to retake the quiz when you feel like it.\nI am always here, ready to help! \nHave a nice day.")
                break
    if tot<2:
        print("Happy news. Your score is "+str(tot)+ ". This shows no apparent problem")
    elif tot>=2:
        print("Your score is "+str(tot)+ ". This is considered Clinically Significant.")
    print("This scale is not designed to make a diagnosis of alcohol dependence or take the place of a professional diagnosis. \n If you suspect that you suffer from alcohol dependency, please consult a mental health professional as soon as possible.")
    print("Take care and goodbye.")

if __name__ == "__main__":
     AlcoholDependence()
