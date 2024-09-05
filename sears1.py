import speech_recognition as sr 

import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    print(".......................... listening you...........................")
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            print("recognizing.........")
            query=r.recognize_google(audio,language='eng-in')
            print(f"user said: {query}\n")
            return query
        except Exception as e:
            print(e)
            print("unable to Recognize your voice")
            return"None"
        


import mysql.connector
con = mysql.connector.connect(host = "localhost",user = "root",password = "karanbhatt36604@gmail.com",database = "airline")

if con.is_connected():
        cursor = con.cursor()
        print("sucessfully connected")

def enter_details(f_n):
    speak("enter name   ")
    name = takeCommand()
    if(name == "None" or name == " "):
        speak("please try again")
        enter_details(f_n)
    speak("enter age   ")
    age =takeCommand()
    speak("enter gender   ")
    gender = takeCommand()
    if 'male' in gender or 'female' in gender :
        s = "SELECT * FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(f_n)
        cursor.execute(s)
        data = cursor.fetchall()
        seats = data[0][8]

        update_query = "update flights set NO_OF_SEATS = {} where FLIGHT_NO = '{}' ".format(seats-1,f_n)
        cursor.execute(update_query)
        print(".............................................................")
        p = "INSERT into passengers (p_name,age,gender,flight_no)values('{}',{},'{}','{}')".format(name,age,gender,f_n)
        cursor.execute(p)
        con.commit()
        id = cursor.lastrowid
        print("\n")
        speak("sucessfully booked your flight")
        print("............successfully booked your flight...................")
        speak("your unique id is "+str(id))
        print("your unique id is ",id)
    else:
        speak("please try again")
        enter_details(f_n)
inp = 1
speak("          WELCOME      to SEARS     ")
print("...............WELCOME..................")
while(inp!='exit') :
    speak("  tell me your choice   ")
    speak("1.   want to  book a flight      ")
    speak("2.   want to cancel a flight     " )
    speak("3.   want to  check details       ")
    speak("4.   exit           ")
    inp = takeCommand()
    if 'book' in inp:
        flag = 1
        while(flag == 1):
            speak("please   enter departure point")
            departure = takeCommand()
            speak("you said "+departure)
            if(departure == "None" or departure == " "): 
                speak("please try again")
                continue
            else :
                speak("please  enter your destination")
                destination = takeCommand()
                speak("you said  "+destination)
                if (destination == "None" or destination ==""):
                    speak("please try again")
                    continue
                else :
                    q = "SELECT * FROM FLIGHTS WHERE DEPARTURE = '{}'AND DESTINATION ='{}' ".format(departure,destination)
                    cursor.execute(q)
                    data = cursor.fetchall()
                    if data:
                        speak("airline available form  "+departure+"   to   "+destination+"  are as follows")
                        for row in data:
                            speak("airline name ="+row[1])
                            speak("flight number = "+row[4])
                            speak("time of departure = "+row[5])
                            speak("time of arrival = "+row[6])
                            speak("cost  = "+str(row[7]))
                            speak("number of seats = "+str(row[8]))
                            speak("you can also see these details on screen ")
                            speak("                     ")
                            print("airline name =",row[1])
                            print("flight number = ",row[4])
                            print("time of departure = ",row[5])
                            print("time of arrival = ",row[6])
                            print("cost  = ",row[7])
                            print("no of seats = ",row[8])
                            print("\n")
                        while(1):
                            speak("which flight do you want to choose please provide flight number?")
                            f_n = takeCommand()
                            if (f_n== "None" or departure == " "):
                                speak("you said none")
                                speak("try again!!")
                                continue
                            else:
                                count = 0
                                for row in data:
                                    if f_n.upper() ==row[4]:
                                        count   = 1
                                if count == 1:
                                    enter_details(f_n)
                                    flag =0
                                    break
                                else:
                                    speak("sorry   no flight available with the flight number you provided!!")
                                    continue
                                
                    else:
                        speak("sorry no flight available from "+departure+"to "+destination)
                        break
    elif 'cancel' in inp :
        speak("are you sure you want to cancel your flight ?")
        res = takeCommand()
        if(res == "yes"):
            speak("enter your unique id:    ")
            id1 = takeCommand()
            speak("deleting reservation with unique id"+id1)
            cursor.execute("DELETE FROM passengers WHERE my_id = {}".format(id1))
            con.commit()
            speak("sucessfully cancel your reservation")
            print("sucessfully cancel your reservation")
        else:
            continue
    elif 'check' in inp:
        speak("enter you unique id")
        choice = takeCommand()
        cursor.execute("SELECT *FROM passengers WHERE my_id = {}".format(choice))
        data = cursor.fetchone()
        if data:
            speak("name = "+data[1])
            speak("age = "+str(data[2]))
            speak("gender = "+data[3])
            speak("flight no"+data[4])
            print("name = ",data[1])
            print("age = ",data[2])
            print("gender = ",data[3])
            print("flight no",data[4])
        else:
            speak("sorry no record found with this unique id!!!!")
    elif 'exit' in inp:
        inp = 'exit'
        speak("thankyou for using SEARS")
        print(".........................THANK YOU............................")

    else:
        speak("you said "+inp+"     ")
        speak("sorry!!!!   cannot identify please try again     ")
