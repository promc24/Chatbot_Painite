'''PYTHON CODE FOR PTSD TEST NOT USED'''
ans_choices=["1","2","3","4","5"]
questions=["1.Repeated, disturbing memories, thoughts, or images of a stressful experience from the past?",
              "2.Repeated, disturbing dreams of a stressful experience from the past?",
              "3.Suddenly acting or feeling as if a stressful experience were happening again (as if you were reliving it)?",
              "4.Feeling very upset when something reminded you of a stressful experience from the past?",
              "5.Having physical reactions (e.g., heart pounding, trouble breathing, or sweating) when something reminded you of a stressful experience from the past?",
              "6.Avoid thinking about or talking about a stressful experience from the past or avoid having feelings related to it?",
              "7.Avoid activities or situations because they remind you of a stressful experience from the past?",
              "8.Trouble remembering important parts of a stressful experience from the past?",
              "9.Loss of interest in things that you used to enjoy?",
              "10.Feeling distant or cut off from other people?",
              "11.Feeling emotionally numb or being unable to have loving feelings for those close to you?",
              "12.Feeling as if your future will somehow be cut short?",
              "13.Trouble falling or staying asleep?",
              "14.Feeling irritable or having angry outbursts?",
              "15.Having difficulty concentrating?",
              "16.Being “super alert” or watchful on guard?",
              "17.Feeling jumpy or easily startled?"]

 

def PTSD():
    tot=0
    print("Painite is using the PTSD CheckList – Civilian Version (PCL-C) Questionnaire.")
    print("Below is a list of problems and complaints that people sometimes have in response to stressful life experiences. Please read each one carefully, pick the answer that indicates how much you have been bothered by that problem in the last month.")
    print("Please answer with the following numbers:")
    print("1 = Not at all ")
    print("2 = A little bit")
    print("3 = Moderately")
    print("4 = Quite a bit")
    print("5 = Extremely")
    for question in questions:
        print(question)
        user_ans=input("answer choice:")
        if user_ans in ans_choices :
            tot=tot+int(user_ans)
                
        else:
            print("Sorry, can you please answer with the given numbers?")
            ans = input("Would you like to retry the test?")
            if ans=="yes" or ans=="ok" or ans=="Yes" or ans=="Ok" or ans=="YES" or ans=="OK" :
                PTSD()
                break
            else:
                print("I understand that you made an effort.\nPlease know that you are more than welcome to retake the quiz when you feel like it.\nI am always here, ready to help!\n Have a nice day")
                break

    if tot>=17 and tot<28:
        print ("Happy news. Your score is "+str(tot)+ ". This shows little to no severity.")
    elif tot>=28 and tot<=29:
        print ("Your score is "+str(tot)+ ". This shows that you may be suffering some PTSD symptoms.\nPlease do print your results if you are seeing a therapist for further evaluation. ")
    elif tot>=30 and tot<=44:
        print ("Your score is "+str(tot)+ ". This shows Moderate to Moderately High severity of PTSD symptoms.\nPlease do print your results if you are seeing a therapist for further evaluation.")
    elif tot>=45 and tot<=85:
        print ("Your score is "+str(tot)+ ". This shows High severity of PTSD symptoms.\nPlease do print your results if you are seeing a therapist for further evaluation.")
    print("This scale is not designed to make a diagnosis of PTSD or take the place of a professional diagnosis. \n If you suspect that you suffer from PTSD, please consult a mental health professional as soon as possible.")
    print("Take care and goodbye.")

if __name__ == "__main__":
     PTSD()
'''END OF PYTHON CODE FOR PTSD TEST '''


'''HTML CODE FOR PTSD'''
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
                        
                    </ul>
                </div>
            </div>
        </nav>
        
        <div class = "container">
            <h1 style="text-align: center;">Self-Assessment for Post-Traumatic Stress Disorder</h1>
            <p style="text-align: justify;">Painite is using the PTSD CheckList – Civilian Version (PCL-C) Questionnaire. Below is a list of problems and complaints that people sometimes have in response to stressful life experiences. </p>
            <section id = "test" style="padding-top: 3vh">
                <p>Pick the answer that indicates how much you have been bothered by that problem in the last month.</p>
                <div id = "q1">
                    <p class = "question">1. Repeated, disturbing memories, thoughts, or images of a stressful experience from the past?</p>
                    <label class = "myRadio">Never
                        <input type="radio" value="1" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Rarely
                        <input type="radio" value="2" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="3" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Often
                        <input type="radio" value="4" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Very often
                        <input type="radio" value="5" name="q1">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q2">
                    <p class = "question">2. Repeated, disturbing dreams of a stressful experience from the past?</p>
                    <label class = "myRadio">Never
                        <input type="radio" value="1" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Rarely
                        <input type="radio" value="2" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="3" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Often
                        <input type="radio" value="4" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Very often
                        <input type="radio" value="5" name="q2">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q3">
                    <p class = "question">3. Suddenly acting or feeling as if a stressful experience were happening again (as if you were reliving it)?</p>
                    <label class = "myRadio">Never
                        <input type="radio" value="1" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Rarely
                        <input type="radio" value="2" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="3" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Often
                        <input type="radio" value="4" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Very often
                        <input type="radio" value="5" name="q3">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q4">
                    <p class = "question">4. Feeling very upset when something reminded you of
                    a stressful experience from the past?</p>
                    <label class = "myRadio">Never
                        <input type="radio" value="1" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Rarely
                        <input type="radio" value="2" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="3" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Often
                        <input type="radio" value="4" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Very often
                        <input type="radio" value="5" name="q4">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q5">
                    <p class = "question">5. Having physical reactions (e.g., heart pounding, trouble breathing, or sweating) when something reminded you of a stressful experience from the
                    past?</p>
                    <label class = "myRadio">Never
                        <input type="radio" value="1" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Rarely
                        <input type="radio" value="2" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="3" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Often
                        <input type="radio" value="4" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Very often
                        <input type="radio" value="5" name="q5">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q6">
                    <p class = "question">6. Avoid thinking about or talking about a stressful experience from the past or avoid having feelings related to it?</p>
                    <label class = "myRadio">Never
                        <input type="radio" value="1" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Rarely
                        <input type="radio" value="2" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="3" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Often
                        <input type="radio" value="4" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Very often
                        <input type="radio" value="5" name="q6">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                
                
                <div>
                    <input type = "submit" value = "Submit" id = "submit-button" onclick = "calculate()">
                        </div>
            </section>
            <section id = "result">
                <h3 id = "result-type" style="text-align: center;"></h3>
                <p style="text-align: justify;">This scale is not designed to make a diagnosis of PTSD or take the place of a professional diagnosis. If you suspect that you suffer from PTSD, please consult a mental health professional as soon as possible.Take care and goodbye.</p>
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
                    var count = 0;
                    for(i = 1; i <= 6; i++)
                    {
                        var q = document.getElementsByName("q"+i.toString());
                        var j = 0;
                        for(j = 0; j < 5; j++)
                        {
                            if(q[j].checked)
                            {
                                count++;
                                ans_array[i-1] = q[j].value;
                                ans += parseInt(q[j].value);
                            }
                        }
                    }
                    if(count!=6)
                    {
                      alert("Please answer all questions.");
                      return false;
                    }
                    console.log(ans);
                    
                    // var modalresult = document.getElementById("resultModal");
                    // modalresult.style.display = "block";
                    // document.getElementsByTagName("body")[0].style.background = "blue";
                    
                    var diag;
                    
                    if(ans <=9&&ans>=0) diag = "No PTSD likely"
                    else if(ans<=13 &&ans>=10) diag = "PTSD possible"
                    else if(ans>=14)  diag = "PTSD may be likely"
                    
                    document.getElementById("test").style.display = "none";
                    document.getElementById("result-type").innerHTML = diag;
                    document.getElementById("result").style.display = "block";
                    
                    return true;
                    
                }
            
                </script>
        </div>
    </body>
</html>
'''HTML CODE FOR PTSD test end'''
'''HTML CODE FOR Schizophrenia test'''
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
                <a class="navbar-brand" href="#">Painite</a>
                <img src="/logo.png" ALIGN="justify"/>
                <img src="/icon.png" ALIGN="left" />
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav navbar-right">
                    <li class="active"><a href="https://painite.neocities.org/Home.html">Home</a></li> 
                </ul>
            </div>
        </div>
    </nav>

    <div class = "container">
        <h1 style="text-align: center;">Self-Assessment for Schizophrenia</h1>
        <p style="text-align: justify;">The Schizophrenia Test and Early Psychosis Indicator (STEPI, Version 2011.1) for Prodromal Syndromes and Psychosis is designed as a simple screening quiz to help identify symptoms of the schizophrenia.</p>        
        <section id = "test" style="padding-top: 3vh">
                <div id = "q1">
                    <p class = "question">1. I find it difficult to separate reality from fantasy and delusion. This makes it hard to trust myself or others, because I'm not sure if I am being lied to or controlled.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q1">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q2">
                    <p class = "question">2. Others plot to hurt me. I am being persecuted by a secret group, government, religion, etc. They monitor me everywhere I go.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q2">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q3">
                    <p class = "question">3. I cannot control my own mind, thoughts, or actions for various reasons, including possession, mind control, or lack of willpower.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q3">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q4">
                    <p class = "question">4. I have magical, psychic, or spiritual powers that others do not. They either don't believe me or want to stop me.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q4">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q5">
                    <p class = "question">5. Because of jealousy or fear of my powers, others treat me unkindly and unfairly. For this reason, I do not socialize much.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q5">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q6">
                    <p class = "question">6. I communicate with people, spirits, or entities beyond this world that others cannot see or hear. They gift me secret information or torment and trouble me.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q6">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q7">
                    <p class = "question">7. People disbelieve my knowledge and skill of magical powers, psychic abilities, and conspiracy plots. They think I am 'crazy'.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q7">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q8">
                    <p class = "question">8. My beliefs are so unique or truthful that others find them very bizarre or scary. I am the only one who knows the truth.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q8">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q8">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q8">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q8">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q8">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q8">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q9">
                    <p class = "question">9. I am alone. I have nothing in common with anyone else on the planet, including my family and friends. I am special.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q9">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q9">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q9">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q9">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q9">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q9">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q10">
                    <p class = "question">10. When I express myself, people become confused or think I am strange. They cannot understand me and words, or are scared to do so.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q10">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q10">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q10">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q10">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q10">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q10">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q11">
                    <p class = "question">11. I procrastinate and waste lots of time. Everything is pointless and there is some impending doom lurking in the near future.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q11">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q11">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q11">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q11">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q11">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q11">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q12">
                    <p class = "question">12. My short-term memory is becoming worse and worse. I can't remember simple or big things, such as where I sat my drink or a doctor's appointment.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q12">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q12">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q12">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q12">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="3" name="q12">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="3" name="q12">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q13">
                    <p class = "question">13. I find myself lost in aimless activities that have no purpose or meaning to them. I can waste many hours doing this before I realize what has happened.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q13">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q13">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q13">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q13">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q13">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q13">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q14">
                    <p class = "question">14. My emotions are not appropriate for the events that occur. For example, I cry for no reason or laugh at violence.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q14">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q14">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q14">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q14">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q14">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q14">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q15">
                    <p class = "question">15. I suspect the world is not real, like a puppet show or illusion. A sinister force is responsible for this trickery. They have replaced the people I care about with robots or 'walk-ins.'</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q15">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q16">
                    <p class = "question">16. I spend far too much time in anxiety about existence. I can stare at my hands in wonder and fear for hours. I can't let it go, even though it troubles me.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q16">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q16">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q16">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q16">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q16">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q16">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q17">
                    <p class = "question">17. It occurred to me that if I answer truthfully on this schizophrenia quiz, someone might be tracking the info and use it against me.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q17">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q17">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q17">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q17">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q17">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q17">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q18">
                    <p class = "question">18. My communication skills are deteriorating. I'm losing my vocabulary, grammar, syntax, speech, and even handwriting skills. I mix words, languages, and letters together.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q18">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q18">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q18">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q18">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q18">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q18">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q19">
                    <p class = "question">19. I'm extremely anxious in social situations. I'd rather avoid them. I fear being judged, making a mistake, or offending someone.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q19">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q19">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q19">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q19">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q19">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q19">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q20">
                    <p class = "question">20. The color red makes me angry. The colors blue or green calm me. I can taste and hear things when I look at them. I can feel the colors.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q20">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">A little bit
                        <input type="radio" value="1" name="q20">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Sometimes
                        <input type="radio" value="2" name="q20">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderately
                        <input type="radio" value="3" name="q20">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Frequently
                        <input type="radio" value="4" name="q20">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">All the time
                        <input type="radio" value="5" name="q20">
                            <span class="checkmark"></span>
                            </label>
                </div>

            <div>
              <input type = "submit" value = "Submit" id = "submit-button" onclick = "calculate()">
            </div>
        </section>
        <section id = "result">
          <h3 id = "result-type" style="text-align: center;"></h3>
          <p style="text-align: justify;">Please be noted that this questionnaire can be used to show your doctor how your symptoms have changed from one visit to the next.  Changes of five or more points are significant. This scale is not designed to make a diagnosis of Schizophrenia or take the place of a professional diagnosis.  If you suspect that you suffer from the symptoms, please consult a mental health professional as soon as possible.</p>
          <div>
              <input type = "button" value = "Consult a psychiatrist" id = "consult-button">
          </div>
        </section>
        
        <script type="text/javascript">
            function calculate()
            {
              var ans_array = [];
              var i = 1;
              var count = 0;
              var ans = 0;
              for(i = 1; i <= 20; i++)
              {
                var q = document.getElementsByName("q"+i.toString());
                var j = 0;
                console.log(q[j]);
                for(j = 0; j < 6; j++)
                {
                    if(q[j].checked)
                    {
                      count++;
                      ans_array[i-1] = q[j].value;
                      ans +=parseInt(q[j].value);
                    }
                }
              }
              if(count!=20)
              {
                alert("Please answer all questions.");
                return false;
              }
              console.log(ans);

              // var modalresult = document.getElementById("resultModal");
              // modalresult.style.display = "block";
              // document.getElementsByTagName("body")[0].style.background = "blue";

              var diag;

              if(ans <=30&&ans>=0) diag = "Likely not at risk for schizophrenia"
              else if(ans <= 55&&ans>=31) diag = "Low to moderate schizophrenia"
              else if(ans<= 70&&ans>=56)  diag = "You are experiencing schizophrenic symptoms"
              else if(ans <= 100&& ans>=71) diag = "You are experiencing very acute symptoms of schizophrenia"

              document.getElementById("test").style.display = "none";
              document.getElementById("result-type").innerHTML = diag;
              document.getElementById("result").style.display = "block";

              return true;

            }

        </script>
    </div>
</body>
</html>
''' HTML code for Schizophrenia test end'''

'''The following codes are a modification of the original ones. The python code of the Alcohol dependence and Bipolar Disorder tests were originally written by team members where their original codes are in the history of their files (commited by them) under the names of Mustafa and Wura. I couldn’t highlight or comment next to my work due to the distress of taking credit for most of their work for reforming their code and having my name next to most lines.'''

'''Alcohol dependence test python code (not used), with some of my modifications'''
# The following codes are a modification of the original ones. The python code of the Alcohol dependence was originally written by a team member where their original code is in the history of the Github (commited by them)under the file name:Mustafa.py

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
 
'''Bipolar Disorder test python code (not used), with some of my modifications'''

# The following codes are a modification of the original ones. The python code of the Bipolar Disorder was originally written by a team member where their original code is in the history of the Github (commited by them)under the file name:Wura.py

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
'''Bipolar Disorder test end'''
