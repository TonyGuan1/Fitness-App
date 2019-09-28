from tkinter import *

#List for Sleep Tracker
SleepingHours = []

root = Tk()
root.geometry("340x350") #Set Window Size
root.title("Fitness App")




#Fonts
DFont = ("Times", 15, "bold")

def Exit():
    Exit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if Exit > 0:
        root.destroy() #This stops the program (mainloop)

def floatTest(var1):
        floatTest2 = False
        try:
                float(var1)
                floatTest2 = True
        except ValueError:
                floatTest2 = False
        if floatTest2 == True:
                return True
        else:
                return False


def calories():
        global weight_entry
        global distance_entry
        global caloriesLabel
                           
        output1 = weight_entry.get(1.0, END)
        output2 = distance_entry.get(1.0, END)
        floatTest(output1)
        floatTest(output2)
        if floatTest(output1) == True and floatTest(output2) == True:
                output1 = float(output1)
                output2 = float(output2)
                output3 = 0.375 *output1 * output2
                caloriesLabel.configure(text=output3)
        else:
                caloriesLabel.configure(text = "Please enter valid numbers.")
                
#Workout Windows inside "WorkoutWindow"
def CalorieCalculator():
        CalorieCalculator = Toplevel()
        
        global weight_entry
        global distance_entry
        global caloriesLabel

        CalorieCalculator.title("Calorie Calculator")

        CalorieLabel = Label(CalorieCalculator, text="Input your weight and how much you ran. \n We will let you know how many calories you burned.")
        CalorieLabel.grid(row=0, columnspan=2)

        weight = Label(CalorieCalculator, text = "How far did you run(km)?" )
        weight.grid(sticky=W, row = 1)
        weight_entry = Text(CalorieCalculator,width=20,height=1)
        weight_entry.grid(row = 1, column = 1)
        
        distance= Label(CalorieCalculator, text = "Weight(lb):")
        distance.grid(sticky=W, row = 2)
        distance_entry= Text(CalorieCalculator,width=20,height=1)
        distance_entry.grid(row=2, column =1)

        caloriesLabel = Label(CalorieCalculator, text = "")
        caloriesLabel.grid(row=3, column = 1)
        convert = Button(CalorieCalculator, text = "How many calories burned?", command=calories)
        convert.grid(row=3)


def WorkoutWindow(): #Different Types of worksouts

        WorkOuts = Toplevel()
        WorkOuts.title("Workouts")
        WorkOuts.geometry("340x250")

        workoutFrameTitle = Frame(WorkOuts, width=350, height=10, bd=14, relief="raised")
        workoutFrameTitle.pack(side=TOP, fill=X)
        
        #Frames for workout window
        WorkOutFirstFrame = Frame(WorkOuts,width = 200,height = 120,bg = "red")
        WorkOutFirstFrame.pack(side = TOP, fill=X)

        WorkOutSecondFrame = Frame(WorkOuts,width = 200,height = 120,bg = "blue")
        WorkOutSecondFrame.pack(side = TOP, fill=X,)
        
        #Workout Window Title
        WorkOutsTitle = Label(workoutFrameTitle, font=('Times',25,"bold"), text="Workouts", bd=10)
        WorkOutsTitle.pack()

        #Frames for Button

        WOB1FA = Frame(WorkOutFirstFrame, width=170, height=70, bd=8, relief="raise")
        WOB1FA.pack(side = LEFT)

        WOB1FB = Frame(WorkOutFirstFrame, width=170, height=70, bd=8, relief="raise")
        WOB1FB.pack(side = RIGHT)

        WOB2FA = Frame(WorkOutSecondFrame, width=170, height=70, bd=8, relief="raise")
        WOB2FA.pack(side = LEFT)
        
        WOB2FB = Frame(WorkOutSecondFrame, width=170, height=70, bd=8, relief='raise')
        WOB2FB.pack(side = RIGHT)

        #Buttons

        WB1BA = Button(WOB1FA,font = DFont,text=" Core",fg = "black",
             command = AbsWindow, width=12,pady=14)

        WB1BB = Button(WOB1FB,font = DFont,text=" Arms",fg = "black",
             command = ArmsWindow, width=12,pady=14)
       
        WB2BA = Button(WOB2FA,font = DFont,text=" Legs",fg = "black",
             command = LegsWindow, width=12,pady=14)
        
        WB2BB = Button(WOB2FB,font = DFont,text=" Cardio",fg = "black",
             command = CardioWindow, width=12,pady=14)

        #Display Buttons
        
        WB1BA.pack()
        WB1BB.pack()
        WB2BA.pack()
        WB2BB.pack()
        


#Workout Popup Windows
def ArmsWindow(): #Arms Workout Window
        ArmsWindow = Toplevel()
        ArmsWindow.title(" Arms Workout")
        Armtop = Frame(ArmsWindow, width=350, height=10, bd=14, relief="raised")
        Armtop.pack(side=TOP, fill=X)
        ArmLabel = Label(Armtop, font=('Times',25,"bold"), text="Arm Workouts", bd=10)
        ArmLabel.pack()

        ArmWorkMid = Frame(ArmsWindow)
        ArmWorkMid.pack(side=TOP, fill=X)
        ArmTitle1 = Label(ArmWorkMid, font=('Times',15), text="Exercise #1 Pushups\n")
        ArmTitle1.pack()
        ArmWork1 = Label(ArmWorkMid, font=('Times',15), text= ArmW1, justify = LEFT)
        ArmWork1.pack()

        PushupLink = Label(ArmsWindow, text = "Pushup Demonstration",cursor="hand2",fg="blue")
        PushupLink.pack()
        PushupLink.bind("<Button-1>",PushLink)

        ArmWorkBot = Frame(ArmsWindow)
        ArmWorkBot.pack(side=TOP, fill=X)
        ArmTitle2 = Label(ArmWorkBot, font=('Times',15), text="\nExercise #2 Tricep Dips\n")
        ArmTitle2.pack()
        ArmWork2 = Label(ArmWorkBot, font=('Times',15), text= ArmW2, justify = LEFT)
        ArmWork2.pack()

        ArmBut = Frame(ArmsWindow,width=350, height=10, bd=14, relief="raised")
        ArmBut.pack(side=BOTTOM)
        ArmExplainBut = Button(ArmBut, font=('Times',25,"bold"), text="Exercise Explanations", bd=10, command = ArmWindowExp)
        ArmExplainBut.pack()

        TricepDipLink = Label(ArmsWindow, text = "Tricep Dip Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",TricepLink)

        
#Functions for GIfs
def PushLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/odQDebj.gif', new = 2)
def TricepLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/UpQMsHB.gif', new = 2)

ArmW1 = """1. Get ready for the exercise in pushup position
2. Bend elbows and lower body to mat 
3. Push up using palms back to pushup position
4. Repeat until exhaustion\n"""

ArmW2 = """1. Setup by sitting on the floor
2. Have a box behind you for Triceps
3. Straighten Arms to lift your butt off the ground
4. Lower back down without touching ground
5. Keep heels on the gournd
6. Repeat till exhaustion\n"""


def ArmWindowExp(): #Arm Workouts Explanation
        ArmWindowExp = Toplevel()
        ArmWindowExp.title("Arm Workouts Explanation")
        
        #Frames and labels to show all the content

        ArmTopExp = Frame(ArmWindowExp,width=350, height=10, bd=14, relief="raised")
        ArmTopExp.pack(side=TOP, fill=X)
        ArmLabelExp = Label(ArmTopExp, font=('Times',25,"bold"), text="Arm Workouts Explained", bd=10)
        ArmLabelExp.pack()

        ArmWorkMidExp = Frame(ArmWindowExp)
        ArmWorkMidExp.pack(side=TOP, fill=X)
        ArmTitle1Exp = Label(ArmWorkMidExp, font=('Times',15), text="Pushups Explanation\n")
        ArmTitle1Exp.pack()
        ArmWork1Exp = Label(ArmWorkMidExp, font=('Times',15), text= ArmExpW1, justify = LEFT)
        ArmWork1Exp.pack()

        ArmWorkBotExp = Frame(ArmWindowExp)
        ArmWorkBotExp.pack(side=TOP, fill=X)
        ArmTitle2Exp = Label(ArmWorkBotExp, font=('Times',15), text="\nTricep Dips Explanation\n")
        ArmTitle2Exp.pack()
        ArmWork2Exp = Label(ArmWorkBotExp, font=('Times',15), text= ArmExpW2, justify = LEFT)
        ArmWork2Exp.pack()
#Text for Arms Explanation
ArmExpW1 = """1. Trains multiple parts of the body
2. Helps with cardiovascular health
3. Improves body and muscle definition
4. Can improve posture 
5. Helps prevent shoulder and back injuries"""
ArmExpW2 = """1. Dips are very good at strengthening triceps
2. Can be varied in many ways for different benefits
3. Can help to define muscles and build a toned body
4. Can be done anywhere no equipment"""

def LegsWindow(): # Leg Workouts Window
        LegsWindow = Toplevel()
        LegsWindow.title(" Legs Workout")
        LegTop = Frame(LegsWindow,width=350, height=10, bd=14, relief="raised")
        LegTop.pack(side=TOP, fill=X)
        LegLabel = Label(LegTop, font=('Times',25,"bold"), text="Leg Workouts", bd=10)
        LegLabel.pack()

        LegWorkMid = Frame(LegsWindow)
        LegWorkMid.pack(side=TOP, fill=X)
        LegTitle1 = Label(LegWorkMid, font=('Times',15), text="Exercise #1 Hop Tuck\n")
        LegTitle1.pack()
        LegWork1 = Label(LegWorkMid, font=('Times',15), text= LegW1, justify = LEFT)
        LegWork1.pack()

        TricepDipLink = Label(LegsWindow, text = "Hop Tuck Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",HopTuckLink)

        LegWorkBot = Frame(LegsWindow)
        LegWorkBot.pack(side=TOP, fill=X)
        LegTitle2 = Label(LegWorkBot, font=('Times',15), text="\nExercise #2 Stair Taps\n")
        LegTitle2.pack()
        LegWork2 = Label(LegWorkBot, font=('Times',15), text= LegW2, justify = LEFT)
        LegWork2.pack()

        LegBut = Frame(LegsWindow,width=350, height=10, bd=14, relief="raised")
        LegBut.pack(side=BOTTOM)
        LegExplainBut = Button(LegBut, font=('Times',25,"bold"), text="Exercise Explanations", bd=10, command = LegWindowExp)
        LegExplainBut.pack()

        TricepDipLink = Label(LegsWindow, text = "Stair Taps Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",StairTapsLink)
#Functions for Gifs
def HopTuckLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/ygp9wxj.gif', new = 2)
def StairTapsLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/wvnbSCh.gif', new = 2)
#Text for Leg Workouts
LegW1 = """1. Stand with feet hip width apart
2. Keep knees soft, arms at shoulder level
3. Squat until knees are at 90 degrees
4. Jump bringing knees toward chest
5. Grab knees with hand in mid air
6. Repeat for 30 Seconds\n"""

LegW2 = """1. Stand facing a box or bench
2. Keep elbows bent at sides
3. Put your hands in front of you
4. Tap one foot on the bench
5. Then Tap your other foot on the bench
6. Quickly alternate taps
7. Continue Exercise for 1 Minute\n"""

def LegWindowExp(): #Leg Workouts Explanation
        LegWindowExp = Toplevel()
        LegWindowExp.title("Legs Workout Explanation")

        LegTopExp = Frame(LegWindowExp,width=350, height=10, bd=14, relief="raised")
        LegTopExp.pack(side=TOP, fill=X)
        LegLabelExp = Label(LegTopExp, font=('Times',25,"bold"), text="Leg Workouts Explained", bd=10)
        LegLabelExp.pack()

        LegWorkMidExp = Frame(LegWindowExp)
        LegWorkMidExp.pack(side=TOP, fill=X)
        LegTitle1Exp = Label(LegWorkMidExp, font=('Times',15), text="Hop Tuck Explanation\n")
        LegTitle1Exp.pack()
        LegWork1Exp = Label(LegWorkMidExp, font=('Times',15), text= LegExpW1, justify = LEFT)
        LegWork1Exp.pack()

        LegWorkBotExp = Frame(LegWindowExp)
        LegWorkBotExp.pack(side=TOP, fill=X)
        LegTitle2Exp = Label(LegWorkBotExp, font=('Times',15), text="\nStair Taps Explanation\n")
        LegTitle2Exp.pack()
        LegWork2Exp = Label(LegWorkBotExp, font=('Times',15), text= LegExpW2, justify = LEFT)
        LegWork2Exp.pack()
#Text for Legs Explanations
LegExpW1 = """1. Strengthens many different parts of the body
2. Makes calves, glutes, hamstrings and quads much stronger
3. Reduces Stiffness and leg pain
4. Can help to melt away stubborn fat
5. It helps to boost memory levels"""
LegExpW2 = """1. Works many parts of your leg
2. Burns a lot of calories as you move your body
3. Can increase cardiovascular health
4. Helps people increase endurace and peformance
5. Develops quadriceps, glutes, calves core and much more"""

def CardioWindow(): #Cardio Workout Window
        CardioWindow = Toplevel()
        CardioWindow.title("Cardio Workout")
        CardioTop = Frame(CardioWindow,width=350, height=10, bd=14, relief="raised")
        CardioTop.pack(side=TOP, fill=X)
        CardioLabel = Label(CardioTop, font=('Times',25,"bold"), text="Cardio Workouts", bd=10)
        CardioLabel.pack()

        CardioWorkMid = Frame(CardioWindow)
        CardioWorkMid.pack(side=TOP, fill=X)
        CardioTitle1 = Label(CardioWorkMid, font=('Times',15), text="Exercise #1 On Spot Jogging\n")
        CardioTitle1.pack()
        CardioWork1 = Label(CardioWorkMid, font=('Times',15), text= CardioW1, justify = LEFT)
        CardioWork1.pack()

        TricepDipLink = Label(CardioWindow, text = "Jogging Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",JoggingLink)

        CardioWorkBot = Frame(CardioWindow)
        CardioWorkBot.pack(side=TOP, fill=X)
        CardioTitle2 = Label(CardioWorkBot, font=('Times',15), text="\nExercise #2 Mountain Climbers\n")
        CardioTitle2.pack()
        CardioWork2 = Label(CardioWorkBot, font=('Times',15), text= CardioW2, justify = LEFT)
        CardioWork2.pack()

        CardioBut = Frame(CardioWindow,width=350, height=10, bd=14, relief="raised")
        CardioBut.pack(side=BOTTOM)
        CardioExplainBut = Button(CardioBut, font=('Times',25,"bold"), text="Exercise Explanations", bd=10, command = CardioWindowExp)
        CardioExplainBut.pack()

        TricepDipLink = Label(CardioWindow, text = "Mountain Climbers Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",MountainClimbersLink)
        
#Link to GIF
def JoggingLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/kbWGqu7.gif', new = 2)
def MountainClimbersLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/tmpKu2t.gif', new = 2)
#Text for Cardio window     
CardioW1 = """1. Keep feet shoulder width apart
2. Move arms while jogging
3. Lift knees higher for a bigger challenge
4. Increase speed (More Calories)
5. Jog Intensely for small periods
6. Jog for 2 minutes or till exhaustion\n"""

CardioW2 = """1. Start by resting in pushup position
2. Keep one foot closer to hands
3. Jump your other foot and alternate hands
4. Find a suitable rythm
5. Repeat for 1 minute\n"""

def CardioWindowExp(): #Cardio Workout Explanation
        CardioWindowExp = Toplevel()
        CardioWindowExp.title("Cardio Workout Explanation")

        CardioTopExp = Frame(CardioWindowExp,width=350, height=10, bd=14, relief="raised")
        CardioTopExp.pack(side=TOP, fill=X)
        CardioLabelExp = Label(CardioTopExp, font=('Times',25,"bold"), text="Cardio Workouts Explained", bd=10)
        CardioLabelExp.pack()

        CardioWorkMidExp = Frame(CardioWindowExp)
        CardioWorkMidExp.pack(side=TOP, fill=X)
        CardioTitle1Exp = Label(CardioWorkMidExp, font=('Times',15), text="On Spot Jogging Explanation\n")
        CardioTitle1Exp.pack()
        CardioWork1Exp = Label(CardioWorkMidExp, font=('Times',15), text= CardioExpW1, justify = LEFT)
        CardioWork1Exp.pack()

        CardioWorkBotExp = Frame(CardioWindowExp)
        CardioWorkBotExp.pack(side=TOP, fill=X)
        CardioTitle2Exp = Label(CardioWorkBotExp, font=('Times',15), text="\nMountain Climbers Explanation\n")
        CardioTitle2Exp.pack()
        CardioWork2Exp = Label(CardioWorkBotExp, font=('Times',15), text= CardioExpW2, justify = LEFT)
        CardioWork2Exp.pack()
#Text for Cardio Explanations
CardioExpW1 = """1. Same benefits as running on treadmill
2. Can be entertaining, watch tv while jogging
3. Convenience, you dont have to go to gym
4. Helps with prevention of disease
5. Can help to incrase weight loss"""
CardioExpW2 = """1. Builds lower body strength
2. Works on multiple parts of body at the same time
3. Helps with cardiovascular health
4. Can improve overall coordination
5. Involve movement so can help with joing agility"""

def AbsWindow(): #Core Workout Window
        AbsWindow = Toplevel()
        AbsWindow.title("Ab Workouts")

        AbsTop = Frame(AbsWindow,width=350, height=10, bd=14, relief="raised")
        AbsTop.pack(side=TOP, fill=X)
        AbsLabel = Label(AbsTop, font=('Times',25,"bold"), text="Ab Workouts", bd=10)
        AbsLabel.pack()

        AbsWorkMid = Frame(AbsWindow)
        AbsWorkMid.pack(side=TOP, fill=X)
        AbsTitle1 = Label(AbsWorkMid, font=('Times',15), text="Exercise #1 Plank Taps\n")
        AbsTitle1.pack()
        AbsWork1 = Label(AbsWorkMid, font=('Times',15), text= AbsW1, justify = LEFT)
        AbsWork1.pack()

        TricepDipLink = Label(AbsWindow, text = "Plank Tap Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",PlankTapLink)

        AbsWorkBot = Frame(AbsWindow)
        AbsWorkBot.pack(side=TOP, fill=X)
        AbsTitle2 = Label(AbsWorkBot, font=('Times',15), text="\nExercise #2 Lateral Plank Walk\n")
        AbsTitle2.pack()
        AbsWork2 = Label(AbsWorkBot, font=('Times',15), text= AbsW2, justify = LEFT)
        AbsWork2.pack()

        AbsBut = Frame(AbsWindow,width=350, height=10, bd=14, relief="raised")
        AbsBut.pack(side=BOTTOM)
        AbsExplainBut = Button(AbsBut, font=('Times',25,"bold"), text="Exercise Explanations", bd=10, command = AbsWindowExp)
        AbsExplainBut.pack()

        TricepDipLink = Label(AbsWindow, text = "Lateral Plank Walk Demonstration",cursor="hand2",fg="blue")
        TricepDipLink.pack()
        TricepDipLink.bind("<Button-1>",LateralWalkLink)

def PlankTapLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/9PS4xzT.mp4', new = 2)
def LateralWalkLink (event): 
        import webbrowser
        webbrowser.open('http://i.imgur.com/9YDdYh6.mp4', new = 2)
#Text for Abs number 2
AbsW1 = """1. Start in plank position
2. Keep feet shoulder width apart and back low
3. Tap shoulder opposite to hand 
4. Alternate between hands, pick a desired pace
5. Continue for 1 minute or until tired\n"""
AbsW2 = """1. Start out in plank position
2. Keep abs and wrists tight
3. Step right foot and hand to right side
4. Immediately follow with left foot and hand
5. Take a few "steps" in a certain direction
6. take a few "steps" in the opposite direction
7. Continue for 1 minute\n"""


def AbsWindowExp(): #Core workout Explanation
        AbsWindowExp = Toplevel()
        AbsWindowExp.title("Ab Workout Explanation")

        AbsTopExp = Frame(AbsWindowExp,width=350, height=10, bd=14, relief="raised")
        AbsTopExp.pack(side=TOP, fill=X)
        AbsLabelExp = Label(AbsTopExp, font=('Times',25,"bold"), text="Ab Workouts Explained", bd=10)
        AbsLabelExp.pack()

        AbsWorkMidExp = Frame(AbsWindowExp)
        AbsWorkMidExp.pack(side=TOP, fill=X)
        AbsTitle1Exp = Label(AbsWorkMidExp, font=('Times',15), text="Plank Taps Explanation\n")
        AbsTitle1Exp.pack()
        AbsWork1Exp = Label(AbsWorkMidExp, font=('Times',15), text= AbsExpW1, justify = LEFT)
        AbsWork1Exp.pack()

        AbsWorkBotExp = Frame(AbsWindowExp)
        AbsWorkBotExp.pack(side=TOP, fill=X)
        AbsTitle2Exp = Label(AbsWorkBotExp, font=('Times',15), text="\nLateral Plank Walk Explanation\n")
        AbsTitle2Exp.pack()
        AbsWork2Exp = Label(AbsWorkBotExp, font=('Times',15), text= AbsExpW2, justify = LEFT)
        AbsWork2Exp.pack()
        
#Text for Abs window
AbsExpW1 = """1. Planking helps to build your core muscles
2. It works the core and that helps to reduce back pain
3. This exercise helps to increase flexibility
4. Exercise in general can improve mood
5. By engaging abs posture and balance will improve"""
AbsExpW2 = """1. It challenges multiple parts of your body
2. Help to improve looks, shapes shoulders and define deltoids
3. Strengthening core can reduce chance of injury
4. Can help with coordination"""

def floatTest3(var2): #Test if input is a float for Sleep Calculator
        floatTest3 = False
        try:
                float(var2)
                floatTest3 = True
        except ValueError:
                floatTest3 = False
        if floatTest3 == True:
                return True
        else:
                return False

def SleepCalculator():#
        if len(SleepingHours) == 0:
                S_Cal_instruct.configure(text = "Try again, after entering a value.")

        else:
                S_Cal_instruct
                X = list(map(float,SleepingHours))#Changes the list elements into float
                Y= sum(X)
                print (Y)
                SleepAvg = Y / len(X)
                if 10 >= SleepAvg >= 24:
                    S_Cal_instruct.configure(text = round(SleepAvg,2))
                    S_Cal_AvgLabel.configure (text = "You Should Sleep Less")
                elif  7.99 <= SleepAvg <= 10:
                    S_Cal_instruct.configure(text = round(SleepAvg,2))
                    S_Cal_AvgLabel.configure (text = "You Are Sleeping Well")
                elif 0<= SleepAvg <= 7.99:
                    S_Cal_instruct.configure(text = round(SleepAvg,2))
                    S_Cal_AvgLabel.configure (text = "You Should Sleep More")
                else:
                    S_Cal_instruct.configure(text = round(SleepAvg,2))
                    S_Cal_AvgLabel.configure (text = "Invalid Input")   
                  
def DelSleep (): #Clears SleepingHours List
        global S_Cal_instruct
        global S_Cal_AvgLabel
        
        del SleepingHours[:]
        S_Cal_AvgLabel.configure (text = "")
        S_Cal_instruct.configure (text = "Your list has been cleared.")
        

def AddSleep (): #Adds to SleepingHours List
        
        global S_Cal_instruct
        global S_Cal_AvgLabel
        ADD = S_Cal_Entry.get()
        floatTest3(ADD)
        if floatTest3(ADD) == True:
                SleepingHours.append(S_Cal_Entry.get())
                print (SleepingHours)
                S_Cal_instruct.configure(text="Your hour has been added.")
        else:
                S_Cal_instruct.configure(text = "Please enter numerical values only.")
                
def SleepTracker(): #Sleep Tracker Window

        
        global S_Cal_Entry
        global TotalSleep
        global S_Cal_instruct
        global S_Cal_AvgLabel
        
        SleepTracker = Toplevel()
        SleepTracker.title("Sleep Calculator")
        
        S_Cal = Label(SleepTracker,text="How many hours have \nyou slept in the past few days?  ")
        S_Cal.grid(row = 0, columnspan=4)
        
        S_Cal_instruct = Label(SleepTracker, text = "When ready, use average to calculate.")
        S_Cal_instruct.grid (row = 2, columnspan = 4)
        
        
        S_Cal_Entry = Entry(SleepTracker,width=20)
        S_Cal_Entry.grid (row = 1, column = 0)

       
        S_Cal_Button = Button(SleepTracker,text= "Average",command = SleepCalculator)
        S_Cal_Button.grid(row = 1,column = 1,sticky = E)


        S_Cal_Button_Add = Button(SleepTracker,text= "Add",command = AddSleep)
        S_Cal_Button_Add.grid(row = 1,column = 2,sticky = E)

  
        S_Cal_Button_Del = Button(SleepTracker,text = "Clear List", command = DelSleep)
        S_Cal_Button_Del.grid(row = 1, column = 3, sticky = E)


        S_Cal_AvgLabel = Label(SleepTracker,text= "")
        S_Cal_AvgLabel.grid (row = 2, column= 0, sticky = W)


def BMICalculator(): #Calculations for the BMI
    
        global BMI_Weight_Entry
        global BMI_Height_Entry
        global BMI_Display_Label
        global BMI_output
        
        bmi_output1 = BMI_Weight_Entry.get(1.0, END)
        bmi_output2 = BMI_Height_Entry.get(1.0, END)
        
        floatTest(bmi_output1)
        floatTest(bmi_output2)
        
        if floatTest(bmi_output1) == True and floatTest(bmi_output2) == True: #Checks if input from BMI is a float, if it is, continue 
                bmi_output1 = float(bmi_output1)
                bmi_output2 = float(bmi_output2)
                BMI_output  = round(bmi_output1 / bmi_output2**2 * 703,2)
                BMI_Display_Label.configure(text=BMI_output)
                bmiIndicator()
        else:
                BMI_Display_Label.configure(text = "Please enter valid numbers.")

def bmiIndicator():#Outputs your BMI level
        
        global BMI_output
        global BMI_Indicator_Label
        
        if BMI_output < 13:
                BMI_Indicator_Label.configure(text="This is very unhealthy.")
        elif BMI_output < 19:
                BMI_Indicator_Label.configure(text="This is unhealthy.")
        elif BMI_output < 24:
                BMI_Indicator_Label.configure(text="This is normal.")
        elif BMI_output < 29:
                BMI_Indicator_Label.configure(text="You are overweight.")
        elif BMI_output < 39:
               BMI_Indicator_Label.configure (text="You are obese.")
        else:
             BMI_Indicator_Label.configure(text="bro u fat.")
                     
                
def BMIWindow():#Everything for the BMI Window
        bmi = Toplevel()
        bmi.title("BMI Calculator")
        
        global BMI_Weight_Entry
        global BMI_Height_Entry
        global BMI_Display_Label
        global BMI_Indicator_Label
        
        BMI_Label = Label(bmi, text="Input your weight and height \n We will let you know your BMI (Body Mass Index).")
        BMI_Label.grid(row=0, columnspan=2)
        
        BMI_Weight = Label(bmi, text = "Weight(lb):" )
        BMI_Weight.grid(sticky=E, row = 1)
        
        BMI_Height= Label(bmi, text = "Height(inches):")
        BMI_Height.grid(sticky=E, row = 2)
        
        BMI_Weight_Entry = Text(bmi,width=20,height=1)
        BMI_Weight_Entry.grid(row = 1, column = 1)
        
        BMI_Height_Entry = Text(bmi,width=20,height=1)
        BMI_Height_Entry.grid(row=2, column =1)

        BMI_Display_Label = Label(bmi, text = "")
        BMI_Display_Label.grid(row=3, column = 1)
        BMI_convert = Button(bmi, text = "Whats your BMI?",command = BMICalculator)
        BMI_convert.grid(row=3)
        
        BMI_Indicator_Label= Label(bmi,text="")
        BMI_Indicator_Label.grid(row=4,columnspan=2)

def Donation (event):
        import webbrowser
        webbrowser.open('https://www.paypal.me/TGuan1', new = 2)


def Info (): #Information Window
        Info = Toplevel()
        Info.title("Info")
        InfoInfo = Label(Info,text =Infotext)
        InfoInfo.pack()
        Infolink = Label(Info, text = "Donate to support us",cursor="hand2",fg="blue")
        Infolink.pack()
        Infolink.bind("<Button-1>",Donation)
        
#Text linked to Information Window
Infotext ="""This is a fitness program, created by
Tony.G, Shashaank.S,
Johnny.L, and Bryan.C """

#Water Intake Calculator
def WaterCalculate ():
        global Water_Weight_Entry
        global Water_Display_Label

        WaterEntry = Water_Weight_Entry.get(1.0,END)
        waterTest(WaterEntry)
        if waterTest(WaterEntry) == True:
                Water_Entry_Output = float(WaterEntry)
                WaterFinal  = round(0.5 * Water_Entry_Output,2)
                Water_Display_Label.configure(text=WaterFinal)
        else:
                Water_Display_Label.configure(text = "Please enter valid numbers.")


#Water Intake Window        
def WaterIntake():
        global Water_Display_Label
        global Water_Weight_Entry
        WaterIntake = Toplevel()
        WaterIntake.title("Water Intake")
        
        Water_Weight = Label(WaterIntake, text = "Weight(lb):" )
        Water_Weight.grid(sticky=E, row = 1,column=0)
        
        Water_Weight_Entry = Text(WaterIntake,width=20,height=1)
        Water_Weight_Entry.grid(row = 1, column = 1)
        
        Water_Calculate = Button(WaterIntake,text = "Calculate",command = WaterCalculate)
        Water_Calculate.grid (sticky = E, row= 1 , column = 2)

        Water_Display_Label = Label(WaterIntake, text ="")
        Water_Display_Label.grid(row = 2, column =1)
        
        Water_Display_Intake_Label = Label(WaterIntake, text ="Water Intake (Oz)")
        Water_Display_Intake_Label.grid(row =2, column =0,sticky = W)

        
def waterTest(var3): #For WaterIntake
        floatTest4 = False
        try:
                float(var3)
                waterTest = True
        except ValueError:
                waterTest = False
        if waterTest == True:
                return True
        else:
                return False

#Title Frame
Tops = Frame(root, width=350, height=10, bd=14, relief="raised")
Tops.pack(side=TOP, fill=X)

labelInfo = Label(Tops, font=('Times',25,"bold"), text="Fitness App", bd=10)
labelInfo.pack()

#Frame under Title Frame
FirstFrame = Frame(root,width = 200,height = 50,)
FirstFrame.pack(side = TOP, fill=X)

SecondFrame = Frame(root,width = 200,height = 50,)
SecondFrame.pack(side = TOP, fill=X,)

ThirdFrame = Frame(root,width = 200,height = 50,)
ThirdFrame.pack(side = TOP, fill=X,)

QuitFrame = Frame(root,width = 200,height = 50)
QuitFrame.pack(side= TOP,fill=BOTH)

#Buttons in Frame
f1A = Frame(FirstFrame, width=200, height=10, bd=8, relief="raise")
f1A.pack(side = LEFT)

f1B = Frame(FirstFrame, width=200, height=100, bd=8, relief='raise')
f1B.pack(side = RIGHT,fill=BOTH)

f2A = Frame(SecondFrame, width =200, height = 100, bd= 8, relief="raise")
f2A.pack(side = LEFT)

f2B = Frame(SecondFrame, width =200, height = 100, bd= 8, relief="raise")
f2B.pack(side = RIGHT)

f3A = Frame(ThirdFrame, width =200, height = 100, bd= 8, relief="raise")
f3A.pack(side = LEFT)

f3B = Frame(ThirdFrame, width =200, height = 100, bd= 8, relief="raise")
f3B.pack(side = RIGHT)

Qf = Frame(QuitFrame,width =200, height = 100, bd= 8, relief="raise")
Qf.pack(side = BOTTOM,fill=BOTH)

#Main Window Buttons
b1A = Button(f1A,font = DFont,text="Workouts",fg = "black",
             command = WorkoutWindow, width=12,pady=10,justify= LEFT,)
b1B = Button(f1B,font = ('Times',15,"bold"),text=" Calorie Counter",fg = "black",
             command = CalorieCalculator, width=12,pady=10)
b2A = Button(f2A,font = ('Times',15,"bold"),text=" BMI Calculator",fg = "black",
             command = BMIWindow, width=12,pady=10)
b2B = Button(f2B,font = ('Times',15,"bold"),text=" Sleep Tracker",fg = "black",
             command = SleepTracker, width=12,pady=10)
b3A = Button(f3A,font = ('Times',15,"bold"),text="Water Intake",fg = "black",
             command = WaterIntake , width=12,pady=10)
b3B = Button(f3B,font = ('Times',15,"bold"),text="Info",fg = "black",
             command = Info, width=12,pady=10)
Quit= Button(Qf,font =('Times',15,"bold"),text ="Quit",fg = "black",
             command = Exit)

#Display Buttons

b1A.pack()
b1B.pack()
b2A.pack()
b2B.pack()
b3A.pack()
b3B.pack()
Quit.pack(fill=BOTH)#Fills X and Y axis

#Displays Window
root.mainloop()
