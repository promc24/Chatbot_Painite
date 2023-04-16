'''NOT USED PYTHON CODE ANXIETY TEST'''
def anxietyTest():
    print("Painite uses the Generalized Anxiety Disorder GAD-7 Screening")
    print("During the last 2 weeks, how often have you been bothered by the following problems?")
    print("Please answer with the following numbers:")
    print("0 = not at all ")
    print("1 = several days")
    print("2 = more than half the days")
    print("3 = nearly every day")

    questions = ["1) Feeling nervous, anxious, or on edge", 
             "2) Not being able to stop or control worrying",
             "3) Worrying too much about different things", 
             "4) Trouble relaxing", 
             "5) Being so restless that it is hard to sit still",
             "6) Becoming easily annoyed or irritable",
             "7) Feeling afraid as if something awful might happen"]

    ans_choices = "0,1,2 or 3:"
    tot = 0
    for question in questions:
        print(question)
        user_ans = input(ans_choices)
        if user_ans in ans_choices:
            tot = tot+ int(user_ans)
            #if the user's answer match with the given answer it will add them if not it will ask to retake the test
        else:
            print("Sorry, can you please answer with the given numbers?")
            ans = input("Would you like to retry the test?")
            if ans=="yes" or ans=="ok" or ans=="Yes" or ans=="Ok" or ans=="YES" or ans=="OK" :
                anxietyTest()
                break
            else:
                print("I understand that you made an affort, please comeback when you feel like you want to retake it. I am always here, ready to help!")
                break
    #Scoring and Interpretation of Scores
    print("Your result till now is:") 
    if tot<5:
        print("You don't seem to suffer from anxiety.")
    elif tot>=5 and tot<10:
        print("I think you have mild anxiety.")
    elif tot>=10 and tot<15:
        print("I think you have moderate anxiety.")
    elif tot>=15:
        print("I think you have severe anxiety.")
    print("This scale is not designed to make a diagnosis of anxiety or take the place of a professional diagnosis. \n If you suspect that you suffer from anxiety, please consult with a mental health professional as soon as possible.")
if __name__ == "__main__":
    anxietyTest()

    '''END OF PYTHON CODE ANXIETY TEST'''
    
    
    
    

'''HTML CODE FOR ANXIETY TEST'''
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
        <h1 style="text-align: center;">Self-Assessment for Anxiety</h1>
        <p style="text-align: justify;">Painite uses the Generalized Anxiety Disorder GAD-7 Screening.</p>        
        <section id = "test" style="padding-top: 3vh">
        <p>During the last 2 weeks, how often have you been bothered by the following problems?</p>
                <div id = "q1">
                    <p class = "question">1. Feeling nervous, anxious, or on edge.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q1">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q2">
                    <p class = "question">2. Not being able to stop or control worrying.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q2">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q3">
                    <p class = "question">3. Worrying too much about different things.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q3">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q4">
                    <p class = "question">4. Trouble relaxing.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q4">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q5">
                    <p class = "question">5. Being so restless that it is hard to sit still.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q5">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q6">
                    <p class = "question">6. Becoming easily annoyed or irritable.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q6">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q7">
                    <p class = "question">7. Feeling afraid as if something awful might happen.</p>
                    <label class = "myRadio">Not at all
                        <input type="radio" value="0" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Several days
                        <input type="radio" value="1" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">More than half the days
                        <input type="radio" value="2" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Nearly every day
                        <input type="radio" value="3" name="q7">
                            <span class="checkmark"></span>
                            </label>
                </div>
            <div>
              <input type = "submit" value = "Submit" id = "submit-button" onclick = "calculate()">
            </div>
        </section>
        <section id = "result">
          <h3 id = "result-type" style="text-align: center;"></h3>
          <p style="text-align: justify;">Please be noted that this questionnaire can be used to show your doctor how your symptoms have changed from one visit to the next.  Changes of five or more points are significant. This scale is not designed to make a diagnosis of anxiety or take the place of a professional diagnosis.  If you suspect that you suffer from anxiety, please consult a mental health professional as soon as possible.</p>
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
              for(i = 1; i <= 7; i++)
              {
                var q = document.getElementsByName("q"+i.toString());
                var j = 0;
                for(j = 0; j < 4; j++)
                {
                    if(q[j].checked)
                    {
                      count++;
                      ans_array[i-1] = q[j].value;
                      ans += parseInt(q[j].value);
                    }
                }
              }
              
              if(count!=7)
              {
                alert("Please answer all questions.");
                return false;
              }
              console.log(ans);

              // var modalresult = document.getElementById("resultModal");
              // modalresult.style.display = "block";
              // document.getElementsByTagName("body")[0].style.background = "blue";

              var diag;

              if(ans <=4) diag = "Anxiety unlikely"
              else if(ans <= 9&&ans>=5) diag = "Mild anxiety"
              else if(ans<= 14&&ans>=10)  diag = "Moderate anxiety"
              else if(ans <= 21&& ans>=15) diag = "Severe anxiety"

              document.getElementById("test").style.display = "none";
              document.getElementById("result-type").innerHTML = diag;
              document.getElementById("result").style.display = "block";



            }

        </script>
    </div>
</body>
</html>
'''END HTML CODE ANXIETY TEST'''

'''HTML CODE BIPOLAR TEST'''
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
        <h1 style="text-align: center;">Self-Assessment for Bipolar Disorder</h1>
        <p style="text-align: justify;">Painite is using the Mood Disorder Questionnaire (MDQ). The MDQ was developed by a team of psychiatrists, researchers and consumer advocates to address a critical need for timely and accurate diagnosis of bipolar disorder.</p>        
        <section id = "test" style="padding-top: 3vh">
        <p>Has there ever been a period of time when you were not your usual self and...</p>
                <div id = "q1">
                    <p class = "question">1. ...you felt so good or so hyper that other people thought you were not your normal self or you were so hyper that you got into trouble?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q1">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q1">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q2">
                    <p class = "question">2. ...you were so irritable that you shouted at people or started  fights or arguments?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q2">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q2">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q3">
                    <p class = "question">3. ...you felt much more self-confident than usual?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q3">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q3">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q4">
                    <p class = "question">4. ...you got much less sleep than usual and found that you didn’t really miss it?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q4">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q4">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q5">
                    <p class = "question">5. ...you were more talkative or spoke much faster than usual?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q5">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q5">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q6">
                    <p class = "question">6. ...thoughts raced through your head or you couldn’t slow your mind down?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q6">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q6">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q7">
                    <p class = "question">7. ...you were so easily distracted by things around you that you had trouble concentrating or staying on track?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q7">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q7">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q8">
                    <p class = "question">8. ...you had more energy than usual?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q8">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q8">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q9">
                    <p class = "question">9. ...you were much more active or did many more things than usual?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q9">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q9">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q10">
                    <p class = "question">10. ...you were much more social or outgoing than usual, for example, you telephoned friends in the middle of the night?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q10">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q10">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q11">
                    <p class = "question">11. ...you were much more interested in sex than usual?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q11">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q11">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q12">
                    <p class = "question">12. ...you did things that were unusual for you or that other people might have thought were excessive, foolish, or risky?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q12">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q12">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q13">
                    <p class = "question">13. ...spending money got you or your family in trouble?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q13">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q13">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q14">
                    <p class = "question">If you checked YES to more than one of the above, have several of these ever happened during the same period of time?</p>
                    <label class = "myRadio">Yes
                        <input type="radio" value="1" name="q14">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">No
                        <input type="radio" value="0" name="q14">
                            <span class="checkmark"></span>
                            </label>
                </div>
                
                <div id = "q15">
                    <p class = "question">How much of a problem did any of these cause you - like being unable to work; having family, money or legal troubles; getting into arguments or fights?</p>
                    <label class = "myRadio">No problems
                        <input type="radio" value="0" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Minor problem
                        <input type="radio" value="1" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Moderate problem
                        <input type="radio" value="2" name="q15">
                            <span class="checkmark"></span>
                            </label>
                    <label class = "myRadio">Serious problem
                        <input type="radio" value="3" name="q15">
                            <span class="checkmark"></span>
                            </label>
                </div>
            <div>
              <input type = "submit" value = "Submit" id = "submit-button" onclick = "calculate()">
            </div>
        </section>
        <section id = "result">
          <h3 id = "result-type" style="text-align: center;"></h3>
          <p style="text-align: justify;">Please be noted that this questionnaire can be used to show your doctor how your symptoms have changed from one visit to the next.  Changes of five or more points are significant. This scale is not designed to make a diagnosis of Bipolar syndrome or take the place of a professional diagnosis.  If you suspect that you suffer from symptoms please consult a mental health professional as soon as possible.</p>
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
              for(i = 1; i <= 14; i++)
              {
                var q = document.getElementsByName("q"+i.toString());
                var j = 0;
                for(j = 0; j < 2; j++)
                {
                    if(q[j].checked)
                    {
                      count++;
                      ans_array[i-1] = q[j].value;
                      if(i <= 13)
                        ans += parseInt(q[j].value);
                    }
                }
              }
              
              var j = 0;
              var q = document.getElementsByName("q15");
              for(j = 0; j < 4; j++)
              {
                if(q[j].checked)
                { 
                  count++;
                  ans_array[14] = q[j].value;
                }
              }
              
              if(count!=15)
              {
                alert("Please answer all questions.");
                return false;
              }
              
              console.log(ans_array);
              var m = parseInt(ans_array[13]);
              var n = parseInt(ans_array[14]);
              console.log(ans);
              console.log(m);
              console.log(n);

              // var modalresult = document.getElementById("resultModal");
              // modalresult.style.display = "block";
              // document.getElementsByTagName("body")[0].style.background = "blue";

              var diag;
              
              if(ans>=7&&m==1&&n>=2)
              {
                diag="Tested positive for bipolar disorder";
              }
              else
              {
                diag="Tested negative for bipolar disorder";
              }
              
              document.getElementById("test").style.display = "none";
              document.getElementById("result-type").innerHTML = diag;
              document.getElementById("result").style.display = "block";



            }

        </script>
    </div>
</body>
</html>
'''END HTML CODE BIPOLAR'''
