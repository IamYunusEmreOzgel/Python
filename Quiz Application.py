import random   #I used the sample function to randomly choose between questions.

class Question:          
    def __init__(self,txt,option,answer):   #Constructor
        self.txt = txt
        self.option = option
        self.answer = answer
    
    def Control(self, answer):  #This Method Controls the user's responses.
        answer=answer.upper()    #I've made sure that there is no problem when the user is typing in uppercase or lowercase letters. 
        answer=answer.strip()    #If the user enters white space while logging in, it gives an error. 

        if answer == "":           #If the user left the question blank, the score will not increase or decrease. 
            f=open("ScoreTable.txt","a")
            print("Correct Answer ={}".format(self.answer))
            f.write("Correct Answer ={}\n".format(self.answer))
            f.close()
        elif self.answer == answer:     #Returns 1 if the user answered correctly. 
            f=open("ScoreTable.txt","a")
            print("Your Answer is True ---> {} ".format(self.answer))
            f.write("Your Answer is True ---> {} \n".format(self.answer))
            f.close()
            return 1        
        elif self.answer != answer:     #If the user responded incorrectly, a value of 0 is returned and the correct answer is printed on the screen.
            print("Your Answer is Wrong , Correct Answer Should Have Been {} ".format(self.answer))
            f=open("ScoreTable.txt","a")
            f.write("Your Answer is Wrong , Correct Answer Should Have Been {} \n".format(self.answer))
            f.close()
            return 0  
        
class Test:

    def __init__(self, questions):   #Constructor
        self.questions = questions
        self.score = 0
        self.questionNo = 0
        self.Correct=[]     #keeps correct and incorrect answers inside
        self.Wrong=[]

    def seeTheQuestion(self):             #It is ensured that the question and options are written on the screen and the answer is received. 
        f=open("ScoreTable.txt","a")    
        question = self.questions[self.questionNo]        
        print("\nQuestion {}: {}\n".format(self.questionNo + 1 , question.txt)) #allows the question to be printed on the screen 
        f.write("\nQuestion {}: {}".format(self.questionNo + 1 , question.txt))
        opt=["A","B","C","D","E"]
        
        for q in question.option: #allows the options to be printed on the screen          
            for o in range(5):                   #We print the options one by one. 
                print('{}-){} ' .format(opt[o],q))
                f.write('\n{}-){} ' .format(opt[o],q))
                opt.pop(o)
                break            
        answer = input('Answer : ')               # We get the answer from the user         
        f.write("\nAnswer : {} \n".format(answer))
        answer=answer.upper()  #I enlarged it so that it is not capitalized
        
        while answer not in ["A","B","C","D","E"] :    #If the user enters a response that is not available, it gives an error. 
            if answer=="":                             #The user may have wanted to leave the question blank
                print("You left the question blank ")
                f.write("You left the question blank. \n")
                break         #the user can leave the question blank, this is not included in the options, but it is normal.
            print("The answer you entered is not among the choices..")       
            answer = input('Answer: ')
            answer=answer.upper() #I enlarged it so that it is not capitalized
        
        f.close()
        self.scoring(answer)
        self.progress()
        
    def scoring(self, answer):   #Allows the user to score 
        question = self.questions[self.questionNo]

        if question.Control(answer)==1:  #If the user answered the question correctly, she gets 2 points.
            self.score += 2              #user earned 2 points
            self.Correct.append(answer)    #I added the answer to the list of correct results
        elif question.Control(answer)==0:   #User Loses 1 point if she got the Question wrong.
            self.score -= 1               #user lost 1 point
            self.Wrong.append(answer)      #I added the answer to the list of wrong results
        self.questionNo += 1    #Increases the question number by 1 (otherwise the same question is always asked).

    def progress(self):
        
        if len(self.questions) == self.questionNo:  #Prints the result screen if the test is finished
            self.printScoreTable()
            self.saveTheFile()   #Save the file 
            global temporary
            temporary=self.score  #I used it to check after each round 
        else:                         #Allows New question to be displayed if the test has not finished                          
            totalQuestion = len(self.questions)   #Amount of how many questions will be asked in total 
            questionNo = self.questionNo + 1      

            if questionNo > totalQuestion:        #The test ends when the question number and the total number of questions are equalized.
                print('Test is Over.') 
            else:                                 #Prints the question number of the solved problem.
                print("***********************************************")
                print("\nPress enter to leave the question blank")            
                print('\nQuestion {} of {}'.format(questionNo,totalQuestion)) 
            self.seeTheQuestion()

    def printScoreTable(self):  #Prints the result screen.
        print("---*---*---")
        print('Your Score: ', self.score)
        print("---*---*---")
        
        print("You Answered",len(self.Correct),"Question Correctly")   #prints the number of true false and blank questions
        print("You Answered",len(self.Wrong),"Question Wrongly")
        print("You Left",5-(len(self.Correct)+len(self.Wrong)),"Question Blank")


    def saveTheFile(self):    #this method saves the result to file 
        f=open("ScoreTable.txt","a")
        f.write("---*---*---\n")
        if self.score>=5:           #Failed if user scored less than 5 otherwise successful 
            f.write('Your Score: {}\n' .format(self.score))   
            f.write("Congratulations You Are Successful\n")
        if self.score<5:           
            f.write('Your Score: {}\n' .format(self.score))
            f.write("Unfortunately ,You Are Not Successfully\n")
        f.write("---*---*---\n")    
        f.close()   
# ------------------------------------------------------------------------------------
class Math(Test):
    Question1 = Question("If a+b=-10, a.b What Can Be Minimum  ?", ["9" , "16" , "24" , "25" , "27"] , "A")
    Question2 = Question("What is The Right Triangle Area Formula ? " , ["a.b" , "a.b.c" , "2.pi.r" ,"a*c/2" ,"1/2.a.b"] , "E")
    Question3=Question("How Many Sides Does A Parallelogram Have ?" , ["1" , "2" , "3" , "4" , "5"] , "D")
    Question4=Question("If x+6=13, What is X ?" , ["7" , "13" , "21" , "25" , "30"] , "A")
    Question5=Question("If (x+4)+3.(x-8)=45, What is x ?" , ["5" , "6" , "8" , "12" , "21"] , "A")
    Question6=Question("Which Of The Following is The Decimal Fraction Corresponding To The Rational Number 2/5 ?", ["0.1" , "0.2" , "0.3" , "0.4" , "0.5"], "D")
    Question7=Question("Which Of The Following Decimal Fractions is The Greatest ?" , ["0.44", "0.45", "0.445", "0.44", "0.432"], "B")
    Question8=Question("In 30,596, in Which Place is The 0 ?" , ["Tens" , "Thousands" , "Ones" , "Ten Thousands" , "None Of Them"] , "D")
    Question9=Question("What is The Perimeter Of A Square With Side a ?" , ["a.a" , "a^2" , "1/a" , "2a" , "a/3"] , "A")
    Question10=Question("What is The Result Of (3–6/3+3 )/(–5+6/3+5) ?" , ["1" , "2" , "3" , "4" , "9"] , "B")
    
    defaultQuestion=[Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10] #I gathered all the questions registered by default in a list.
    
    def __init__(self):    #Constructor
        super().__init__(self.defaultQuestion)
        
    def Genarate(self):   #It allows to create a test by randomly selecting 5 questions from the questions registered in the system. 
        global temporary   #It keeps the score of the user in the test that the user is solving now.
        chosen = random.sample(self.defaultQuestion,5)  #Allows 5 questions to be chosen randomly.
        quizMath=Test(chosen) 
        Math.progress(quizMath)
        
        while temporary<5:  #If the user earns less than 5 points, she is allowed to take the same test again
            print("Your Score is {} 5 The Test Will Be Repeated Because it is Less Than 5..".format(temporary)) 
            quizMath = Test(chosen)    #I didn't use random.sample again because I want the same questions asked. 
            Math.progress(quizMath) 
        print("Congratulations! You Have Successfully ....")
        temporary=0  #I set it to 0 so that the scoring starts from 0 in the test to be repeated. 
            
    def Add(self,No):   #I used it to make the user add New questions.  
        que=input("Enter The Question : ") 
        while que=="":
            print("Question Can't Be Empty")             #The user cannot leave the question blank while adding a question.
            que=input("Enter The Question : ") 
        
        opts=[]   # The list in which I will save the choices for the question entered by the user. 
        
        for i in ["A","B","C","D","E"]:       #With the for loop, I have the user enter the options.
            opt=input("Enter Option {}  :  ".format(i))
            opt=opt.strip()   #The user can leave unnecessary spaces at the beginning or at the end when entering the options. 
            opts.append(opt)         
            
        answ=input("Enter The Correct Answer : ")
        answ=answ.upper()
        while answ not in ["A","B","C","D","E"] :                     #If the user enters an answer that is not in the options, it allows to ask again. 
            print("The Answer You Entered is Not Among The Choices..")    
            answ=input("Enter The Correct Answer : ")
            answ=answ.upper()
        
        que=que.strip()      # If the user entered unnecessary blank characters while entering the question and answer, I cleared them 
        answ=answ.strip()        
        No=Question(que,opts,answ)    #I have created a new Question. (The user can add as many questions as he wants when the number will increase by 1 in each round.) 
        self.defaultQuestion.append(No)
# ------------------------------------------------------------------------------------
class Physics(Test):
    Question1 = Question("What Does An Ohm Measure ?", ["Air Resistance" , "Electrical Resistance" , "Light" , "Volume Of Gas" , "Temparature"], "B")
    Question2 = Question("The Ability Of A Substance To Return To its Shape After Being Deformed is Called ______.", ["Elasticity", "Flexibilty", "Metaflex", "integrity","Divison"], "A")
    Question3=Question("The Ability To Do Work is _____", ["Velocity", "Force", "Energy", "Heat", "Done"], "B")
    Question4=Question("The Transfer Of Heat By Means Of The Movement Of A Substance is Known As ?", ["Conduction", "Convection", "Radiation", "Transpiration", "Heat Transfer"], "B")
    Question5=Question("What is The Base SI Unit For Measuring Electric Current?", ["Meter", "Amper", "Litre", "Kilogram", "Mili"], "B")
    Question6=Question("Which Of The Following is The Correct SI Unit Of Temperature??", ["None Of Them", "Fahrenheit", "Rankine", "Celsius", "Kelvin"], "E")
    Question7=Question("What Quantity Does The Kilogram Measure? ", ["Radiation", "Force", "Distance", "Time", "Mass"], "E")
    Question8=Question("The SI Base Unit For Time is", ["1 Second", "1 Hour ","1 Day","1 Week","1 Year"], "A")
    Question9=Question("Convert 22 M/s into Km/Hr", ["79", "78", "77", "76", "75"], "A")
    Question10=Question("The Laws Of Physics Tell Us That Energy is ____:", ["Concerned", "Confusion", "A Conserved", "Constant", "Consinent"], "C")
    
    defaultQuestion=[Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10]
    
    def __init__(self):   #Constructor
        super().__init__(self.defaultQuestion)
    
    def Genarate(self):
        global temporary
        chosen = random.sample(self.defaultQuestion,5)
        quizPhysics=Test(chosen)
        Physics.progress(quizPhysics)
        
        while temporary<5:
            print("Your Score is {}  The test will be repeated because it is less than 5..".format(temporary)) 
            quizPhysics = Test(chosen)   
            Physics.progress(quizPhysics)        
        print("Congratulations! You Have Successfully ....")        
        temporary=0
      
    def Add(self,Add):
        que=input("Enter The Question : ") 
       
        while que=="":
            print("Question Can't Be Empty")            
            que=input("Enter The Question : ") 
        opts=[]          
       
        for i in ["A","B","C","D","E"]:
            opt=input("Enter Option {}  : ".format(i))
            opt=opt.strip()  
            opts.append(opt)   
        
        answ=input("Enter The Correct Answer : ")    
        answ=answ.upper()
        
        while answ not in ["A","B","C","D","E"] :                   
            print("The Answer You Entered is Not Among The Choices..")    
            answ=input("Enter The Correct Answer : ")
            answ=answ.upper()
            
        que=que.strip()      
        answ=answ.strip()
        No=Question(que,opts,answ)
        self.defaultQuestion.append(No)     
# ------------------------------------------------------------------------------------
class ComputerProgramming2(Test):
    Question1 = Question("How To Make a Comment Line For A Single Line in Python ?", ["''''''" , "#" , "/" , "//" , "*" , "$$"] , "B")
    Question2 = Question("Which Of The Following Function Checks in A String That All Characters Are Numeric ?", ["isnumeric()" , "islower()" , "isupper()" , "upper()" , "istitle()"] , "A")
    Question3=Question("What Function Can Be Used To Print Text On The Screen in Python Language ?", ["Scanf" , "Printf" , "Print" , "Prn" , "Scan"] , "C")
    Question4=Question("Which is An Oop Related Term  ?", ["İnheritance" , "Print" , "Function" , "add" , "scanf"] , "A")
    Question5=Question("Which One is Used For Creating Lists ?", ["()" , "[]" , "E3" , "{}" , "!!"] ,"B")
    Question6=Question("Which of The Following Can Be Used As A Variable Name? ", ["1Sayi" , "Sayi1" , "*sayı" , "-sayi" , "43.sayı"] , "B")
    Question7=Question("What is The Extension of Python Files?  ?", [".xsl" , ".Docx" , ".xlsxx" , ".py" , "No Specific Extension"] , "D")
    Question8=Question("Year=2019 What is The Data Type Of The Variable ", ["İnt" , "Float" ,"Numerical" ,"String" , "Design"] , "A")
    Question9=Question("Whichever Means Equal ?", ["==" , "=" , "!=" , ">=" , "<"], "A")
    Question10=Question("Which is Used To Do integer Division ?", ["/" , "**" , "^" , "//" , "^"] , "D")
    
    defaultQuestion=[Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10]
    
    def __init__(self):   #Constructor
        super().__init__(self.defaultQuestion)
        
    def Genarate(self):
        global temporary
        chosen = random.sample(self.defaultQuestion,5)
        quizProgramming=Test(chosen)
        ComputerProgramming2.progress(quizProgramming)
        
        while temporary<5:
            print("Your Score is {} 5 The Test Will Be Repeated Because it is Less Than 5..".format(temporary)) 
            quizProgramming = Test(chosen)   
            ComputerProgramming2.progress(quizProgramming)       
        print("Congratulations! You Have Successfully ....")  
        temporary=0
                
    def Add(self,No):
        que=input("Enter The Question : ") 
        
        while que=="":
            print("Question Can't Be Empty")             
            que=input("Enter The Question : ") 
        opts=[]   #Şıkları tutae
        
        for i in ["A","B","C","D","E"]:
            opt=input("Enter Option {}  : ".format(i))
            opt=opt.strip()  
            opts.append(opt)   
        
        answ=input("Enter The Correct Answer : ")  
        answ=answ.upper()
        
        while answ not in ["A","B","C","D","E"] :                     
            print("The Answer You Entered is Not Among The Choices..")    
            answ=input("Enter The Correct Answer : ")      
            answ=answ.upper()
        que=que.strip()     
        answ=answ.strip()
        No=Question(que,opts,answ)
        self.defaultQuestion.append(No)     
# ------------------------------------------------------------------------------------
mat = Math()   #I created an object for all classes. 
physics = Physics()
programlama=ComputerProgramming2()
# ------------------------------------------------------------------------------------
while True:                                   #I have all the user's work done in an infinite loop. It will continue unless the user wants to finish it.
    f=open("ScoreTable.txt","a")
    print("***************************")
    print("Welcome to The System!!!")
    print("Menu:\nWhich Course Do You Want? \nIf You Want to Choose Mathematics Please Enter 'math' or 'm'.\nIf You Want to Choose Physics Please Enter 'physics' or 'p'.")
    print("If You Want to Choose Computer Programmıng 2 Please Enter 'computer programmıng 2' or 'c'.\nPress q For Exit The Program")
    Selection1=input("Your Choice :")  #User selects course 
    
    if Selection1=="q":   #If the user want to exit the program
        print("********************")
        print("Exit The Program")
        f.write("Exit The Program")
        f.write("\n**********************************************")
        f.close()
        break   
# ------------------------------------------------------------------------------------         
    elif Selection1=="math" or Selection1=="m": #If the user select Math
        while True:
            f=open("ScoreTable.txt","a")
            print("\nYou Choose Mathematics!!!")
            f.write("You Choose Mathematics!!!\n")
            Selection2=input("Press 'q' To Exit The Lesson  \nPress 1 To Take The Exam \nPress 2 To Add A Question \nYour Choice :")
            Selection2=Selection2.lower() #I prevented it from making a capitalization error when setting the user preference 
            
            if Selection2=="q":  #If the user want to exit the program
                print("-*-You Return To The Menu Screen-*-")
                break
            elif Selection2=="1" or Selection2=="one" : #If the user want to Solving questions
                print("You Are Currently Solving Maths Questions....")
                f.write("You Are Currently Solving Maths Questions....\n")
                f.close()
                mat.Genarate()    #I called the test generating method with 5 random questions. 
                break
            elif Selection2=="2" or Selection2=="two":
                queNo=10    #I have made it not to give an error if the user wants to add a question more than once 
                queNo+=1
                mat.Add(queNo) #I called the method that allows the user to add as many questions as they want about the course they are in. 
                print("*****Your Question Added in System*****")
                break
            else :
                print("***************************")
                print("You must enter one of the options requested by the system.")
# ------------------------------------------------------------------------------------          
    elif Selection1=="physics" or Selection1=="p":  #If The User Select Physics
        while True:
            print("You Choose Physics!!!")
            f=open("ScoreTable.txt","a")
            f.write("You Choose Physics!!!\n")
            Selection2=input("Press 'q' To Exit The Lesson  \nPress 1 To Take The Exam \nPress 2 To Add A Question \nYour Choice :")
            Selection2=Selection2.lower() 
            
            if Selection2=="q":
                print("-*-You Return To The Menu Screen-*-")
                break            
            elif Selection2=="1" or Selection2=="one" :
                print("You Are Currently Solving  physics questions...")
                f.write("You Are Currently Solving  physics questions...\n")
                f.close()
                physics.Genarate()
                break            
            elif Selection2=="2" or Selection2=="two":
                queNo=10    
                queNo+=1
                physics.Add(queNo)
                print("*****Your Qeustion Added in System*****")
                break
            else :
                print("***************************")
                print("You must enter one of the options requested by the system.")
# ------------------------------------------------------------------------------------             
    elif Selection1=="computer programming 2" or  Selection1=="c":    #If The User Select Compputer Programming 2         
        while True:
            print("You Choose Computer Programming 2!!!\n")
            f=open("ScoreTable.txt","a")
            f.write("You Choose Computer Programming 2")
            Selection2=input("Press 'q' To Exit The Lesson  \nPress 1 To Take The Exam \nPress 2 To Add A Question \nYour Choice :")
            Selection2=Selection2.lower()  
            
            if Selection2=="q":
                print("-*-You Return To The Menu Screen-*-")
                break           
            elif Selection2=="1" or Selection2=="one" :
                print("You Are Currently Solving Computer Programming 2 Questions...")
                f.write("You Are Currently Solving Computer Programming 2 Questions...\n")
                f.close()
                programlama.Genarate()
                break            
            elif Selection2=="2" or Selection2 == "two":
                queNo=10   
                queNo+=1
                programlama.Add(queNo)
                print("*****Your Question Added in System""****")
                break
            else :
                print("***************************")
                print("You must enter one of the options requested by the system.")
            
    else:       #In case of a different keying while choosing a course, it comes here. 
        print("***************************")
        print("*-*Your Choice is Not Among The Courses*-*")       #If the user makes a wrong keying (if he does not choose one of the M, T, C courses) 
f=open("ScoreTable.txt","a")
f.write("*******************************************************************\n")
f.close()