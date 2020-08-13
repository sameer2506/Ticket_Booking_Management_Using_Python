# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:12:31 2020

@author: Sameer
"""
  
import mysql.connector

def user_signup():
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )

    mycursor = mydb.cursor()
    
    username = input("Enter username :")
    
    sql = "SELECT * FROM USER WHERE username = %s "
    mycursor.execute(sql,(username,))
    username_query = mycursor.fetchall()

    if username_query:
        print("Already registered\n")
        user_signup()
        
        
    firstName = input("Enter first name :")
    lastName = input("Enter last name :")
    password = input("Enter password :")  
    
    sql = "INSERT INTO user (firstName,lastName,username,password,status) VALUES (%s, %s,%s,%s,%s)"
    val = (firstName,lastName,username,password,"active")
    mycursor.execute(sql, val)

    mydb.commit()
    
    print("Registration Successful.\n")
    User()

def buy_ticket(movie_id):
    
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )

    mycursor = mydb.cursor()
    
    sql = "SELECT * FROM movielist WHERE id = %s "
    
    mycursor.execute(sql,(movie_id,))
    
    result = mycursor.fetchall()
    
    if result:
        
        for x in result:
            ticket_count=x[5]
            #ticket_price = x[4]
            
    else:
        print("Invalid movie id..\n")
        
    if ticket_count>0:
        import random
        
        num = int((random.random())*1000)
        
        print("Captcha :",num,"\n")
        
        get_captcha = int(input("Enter captcha :"))
        
        if num==get_captcha:
            ticket_count = ticket_count-1
            sql = "UPDATE movielist SET ticketCount = %s WHERE id = %s "
            
            val = (ticket_count,movie_id)

            mycursor.execute(sql,val)

            mydb.commit()

            print("Ticket bought succesfull.\n")
            import random
            import string
            letters = string.ascii_uppercase
            ticket_id = ''.join(random.choice(letters) for i in range(5))
            print("Ticket id :",ticket_id,"\n")
            
        else:
            print("Incorrect captcha...\n")
            
    else:
        print("No ticket available...\n")
            

def delete_movie_list(id):
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )

    mycursor = mydb.cursor()
    
    sql = "DELETE FROM movielist WHERE id = %s"

    mycursor.execute(sql,(id,))

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted\n")
    

def update_movie_list(id):
    
        mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )

        mycursor = mydb.cursor()
        
        print("1.Movie Name\t2.Actor\t3.Actress\n")
        option = int(input("What you want to modify :"))
        data = input("New data :")
        
        if option==1:
            sql = "UPDATE movielist SET movieName = %s WHERE id = %s "
            
            val = (data,id)

            mycursor.execute(sql,val)

            mydb.commit()

            print(mycursor.rowcount, "record(s) affected\n")
            
        elif option==2:
            sql = "UPDATE movielist SET actor = %s WHERE id = %s "
            
            val = (data,id)

            mycursor.execute(sql,val)

            mydb.commit()

            print(mycursor.rowcount, "record(s) affected\n")

        elif option==3:
            sql = "UPDATE movielist SET actress = %s WHERE id = %s "
            
            val = (data,id)

            mycursor.execute(sql,val)

            mydb.commit()

            print(mycursor.rowcount, "record(s) affected\n")
            
        else:
            print("Invalid option...\n")


def add_movie_list():
    
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )

    mycursor = mydb.cursor()
    
    movieName = input("Enter movie name :")
    movieActor = input("Enter movie actor :")
    movieActress = input("Enter movie actress :")
    ticketPrice = float(input("Enter ticket price :"))
    ticketCount = int(input("Enter total number of ticket :"))
    
    sql = "INSERT INTO movielist (movieName,actor,actress,ticketPrice,ticketCount) VALUES (%s,%s,%s, %s,%s)"
    val = (movieName,movieActor,movieActress,ticketPrice,ticketCount)
    mycursor.execute(sql, val)

    mydb.commit()

    show_movie_list()

    print(mycursor.rowcount, "record inserted.\n")

def show_movie_list():
    
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )

    mycursor = mydb.cursor()
    
    mycursor.execute ("SELECT * FROM movielist ")
    
    result = mycursor.fetchall()
    
    for x in result:
        print(x)

def user_login():
    
    usernameInput = input("Enter username :")
    passwordInput = input("Enter password :")
    
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )
    mycursor = mydb.cursor()
    
    admin_query = "SELECT * FROM user WHERE username = %s "
    
    status = "active"
    
    mycursor.execute(admin_query,(usernameInput,))
    
    user_login_db = mycursor.fetchall()
    
    if user_login_db:
        
        for x in user_login_db:
            db_status = x[5]
            db_firstName_user = x[1]
            
        print("Welcome ",db_firstName_user,"\n")
        
            
        if status==db_status:
            #print("Your account is activated. You may preoceed later")
            
            for x in user_login_db:
                db_password = x[4]
                #print(db_password)
                
            if db_password==passwordInput:
                #print("Your password is correct")
                
                show_movie_list()
                
                movie_id = int(input("Enter id of movie to buy ticket :"))
                
                buy_ticket(movie_id)
                
                
            else:
                print("Password incorrect...\n")
            
        else:
            print("Your account is not activated!! Contact owner.\n")
        
    else:
        print("Invalid login....\n")

def Admin():
    print("\t\t\tWelcome to admin section\n")
    
    usernameInput = input("Enter username :")
    passwordInput = input("Enter password :")
    
    mydb = mysql.connector.connect(
        host="	localhost",
        user="	root",
        password="Sameer%cse2020",
        database="ticketbookingmanagement"
        )
    mycursor = mydb.cursor()
    
    admin_query = "SELECT * FROM admin WHERE username = %s "
    
    status = "active"
    
    mycursor.execute(admin_query,(usernameInput,))
    
    admin_login = mycursor.fetchall()
    
    if admin_login:
        
        for x in admin_login:
            db_status = x[5]
            firstName = x[1]
            
        print("Welcome ",firstName,"\n")
            
        if status==db_status:
            #print("Your account is activated. You may preoceed later")
            
            for x in admin_login:
                db_password = x[4]
                #print(db_password)
                
            if db_password==passwordInput:
                #print("Your password is correct")
                print("1.Show Movie List\t2.Add Movie List\t3.Update Movie List\t4.Delete Movie List\n")
                
                admin_activity = int(input("Option :"))
                
                if admin_activity==1:
                    print("\nMovie List.....\n")
                    show_movie_list()
                    
                elif admin_activity==2:
                    #print("Add movie")
                    add_movie_list()
                    
                elif admin_activity==3:
                     #print("update movie")
                     show_movie_list()
                     id = input("Enter id of movie :")
                     update_movie_list(id)
                     
                elif admin_activity==4:
                    #print("delete movie")
                    show_movie_list()
                    id = input("Enter id of movie :")
                    delete_movie_list(id)
                 
                else:
                    print("Invalid option!!\n")

            else:
                print("Password incorrect...\n")
            
        else:
            print("Your account is not activated!! Contact owner.\n")
        
    else:
        print("Invalid login....\n")
    

def User():
    print("\t\t\tWelcome to user section\n")
    
    
    print("1.Login\t2.Signup\n")
    
    option_for_user = int(input("Option :"))
    
    if option_for_user==1:
       user_login()
       
    elif option_for_user==2:
        user_signup()
        print("User Login :\n")
        user_login()
        
    else:
        print("Incorrect option!!\n")
    
    

def welcome():
    print("Welcome to my Ticket Booking System\n")
    print("1.Admin\t2.User\t3.Exit\n")
    option = int(input("Select login type : "))
    
    if option==1:
        Admin()
       # break
    elif option==2:
        User()
       # break
    elif option==3:
        print("Maintainance....\n")
        #exit(0)
    else:
        print("Invalid option!!\n")
    
welcome()

