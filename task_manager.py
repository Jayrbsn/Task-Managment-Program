

#APOLOGIES FOR THE MANY ATTEMPTS TO GET THIS RIGHT...

#If admin selects register new user they will be prompter using input() to create the new username and password and to double check the password
#If the password is not identical both times, there will be an error message and admin will have to start registering the new user again from scratch by means of a while loop
#If the password is identical both times, the new user and their corresponding password will be added to the user.txt file using the write() function
def reg_user():
        
    check_password = ""
    new_password = 3.142*3.142
    
    while check_password != new_password:
        

        import re
        while True:
            new_username = input("Please create your new username: ")
            f = open("user.txt", "r")
            text = f.read()
            re.search(new_username, text)
            if new_username in text:
                print ("\nSorry, that username already exists. Please select a new username")
            else:
                print("name added")
                break
                f.close()
                
        new_password = input("Please create your new password: ")
        check_password = input("Please confirm new password: ")
        new_user_both = f"{new_username}, {new_password}"
        

        if check_password == new_password:
            with open("user.txt", "a") as f:
                f.write("\n"+new_user_both)
                print (f"\nNew user ({new_username}) added! Check 'user.txt'")
                print ("")
                print ("")
        else:
            print("\n *Oops! Your passwords did not match. Please start again*")
            break




#Create function that will run if user types 'gr' into menu bar
#Hopefully I've finally got it right this time
#I seperated the task overview report and user overview report into two seperate functions
#And then created a third function to run both of those functions to allow the program to keep running in case there was some kind of error    
menu_choice = "gr"


#Function for task overview report
def generate_task_overview():
    
    
    #Start by creating the new task_overview.txt file and leaving it open to run more code that will write to it
    task_overview = open("task_overview.txt", "w")
    
    
    
    
    #To state how many tasks are being tracked on the task manager we need to count the number of lines in tasks.txt
    #Open tasks.txt file
    #Use a for loop to count each line and print a message stating how many tasks there are
    #Write results to task_overview file
    with open("tasks.txt", "r") as t:
        q = t.readlines()
        count = 0
        for line in q:
            count += 1
        task_overview.write("Total Number of Tasks on Task Manager: {}".format(count))
    
    
    

    #I modified the below block of code  as per the advice in the last review
    #This should reduce the chances of any index errors barring any cases where a line in the txt file has a missing bit of information
    #To state how many tasks are complete or incomplete, we need to count how many lines end with a 'Yes' or 'No' respectively
    #Open the tasks.txt file
    #Create a list of lines and turn each line into a list of strings
    #Use for loop and indexing to count how many lines end in 'Yes' or 'No'
    #Write results to file
    with open("tasks.txt","r") as f:
        line_count = 0
        yes_count = 0
        no_count = 0
        file = f.readlines()
        for line in file:
            line_list = file[line_count].strip().split(",")
            line_count+=1
            if "n" in line_list[5][0].lower() or "n" in line_list[5][1].lower():
                no_count += 1    
            if "y" in line_list[5][0].lower() or "y" in line_list[5][1].lower():
                yes_count += 1
        task_overview.write("\nTotal Tasks Completed: {}".format(yes_count))
        task_overview.write("\nCurrent Number of Incomplete Tasks: {}".format(no_count))
        
     
    
    
    #I used the below resource to find out how to compare today's date to a date save in the txt file 
    #https://stackoverflow.com/questions/47933270/search-in-text-file-by-date
    #The datetime library helped with this solution
    #Again, create a list of lines and turn each line into a list of strings
    #Use function from the datetime library to compare the date at index[4] for each line to todays date
    #If today's date is greater than what is saved in the txt file
    #Use for loop to count how many tasks are overdue and write information to file
    import datetime
    today = datetime.datetime.today() 
    with open("tasks.txt","r") as f:
        due_count = 0
        overdue_count = 0
        file = f.readlines()
        for line in file:
            line_list = file[due_count].strip().split(",")
            due_count+=1  
            if datetime.datetime.strptime(line_list[4],' %Y-%m-%d') < today:
                overdue_count += 1          
        task_overview.write("\nTotal Overdue Tasks: {}".format(overdue_count))
            
            
            
     
    #Now calculate what percentage of tasks are incomplete or overdue by dividing the incomplete or overdue tasks by the total amount of tasks and multiply by 100
    #Write results to file
    incomplete_percent = (no_count/count)*100
    overdue_percent = (overdue_count/count)*100
    task_overview.write("\nPercentage of Tasks Incomplete: {}".format(incomplete_percent))
    task_overview.write("\nPercentage of Tasks Overdue: {}".format(overdue_percent))
    
    
    
    
    #Close task_overview.txt file now overwritten with all new information
    #Open file again and print the contents for user to see
    task_overview.close()
    task_overview = open("task_overview.txt", "r")
    print ("\nTask Overview Report: \n")
    print(task_overview.read())
    task_overview.close()




#Function for user overview report
def generate_user_overview():
    
    
    #Create and keep open user_overview.txt file
    user_overview = open("user_overview.txt", "w")
    
    
    
    
    #To state how many users are in the database we need to count the lines in user.txt
    #Use for loop to count the lines and write the results to the file
    with open("user.txt", "r") as f:
        user_count = 0
        for line in f:
            user_count += 1
    user_overview.write("Total Number of Registered Users: {}".format(user_count))
    
    
    
    
    #Simply recreate code from earlier to state how many tasks are being tracked
    with open("tasks.txt", "r") as t:
        q = t.readlines()
        count = 0
        for line in q:
            count += 1
        user_overview.write("\nTotal Number of Tasks on Task Manager: {}".format(count))
        
        
        
    
    #To state how many tasks are assigned to the user who is signed in we need to count how many line in tasks.txt start with their username
    #Create a list of line and turn each line into a list of strings
    #All lines who's index[0] matched the variable user_name is relevant to the user
    #Count how many lines are relevant to user and write results to file
    with open("tasks.txt", "r") as f:
        user_line_count = 0
        user_in_line_count = 0
        file = f.readlines()
        for line in file:
            line_list = file[user_line_count].strip().split(",")
            user_line_count += 1
            if username in line_list[0]:
                user_in_line_count += 1
        user_overview.write("\nTotal Number of Tasks Assigned to {}: {}".format(username, user_in_line_count))
        
        
        
    
    #Calculate the percentage of tasks assigned to user using simple math
    #Write result to file
    percent_assignedto_user = (user_in_line_count/count)*100
    user_overview.write("\nPercentage of Tasks Assigned to {}: {}".format(username, percent_assignedto_user))
    
    
    

    #Same modification as the task overview report to reduce index errors
    #To state how many tasks a particular user has complete or incomplete we need to count how many lines have both the user_name at index[0] as well as a 'Yes' or 'No' in tasks.txt
    #Again, turn each line into a list and use indexing to look for the string we want at the relevant index
    #Use for loop to count how many lines meet our criteria for tasks complete or incomplete for a particular user
    #Write results to file
    with open("tasks.txt","r") as f:
        user_line_count2 = 0
        complete_count = 0
        todo_count = 0
        file = f.readlines()
        for line in file:
            line_list = file[user_line_count2].strip().split(",")
            user_line_count2 += 1
            if username in line_list[0] and ("n" in line_list[5][0].lower() or "n" in line_list[5][1].lower()) :
                todo_count += 1    
            if username in line_list[0] and ("y" in line_list[5][0].lower() or "y" in line_list[5][1].lower()):
                complete_count += 1
       
    
    
    user_overview.write("\nTasks Completed by {}: {}".format(username, complete_count))
    user_overview.write("\nTask Left For {}: {}".format(username, todo_count))
        
        
    
    
    #Find out how many tasks relevant to logged in user are overdue:
    #Use same datetime library functions from earlier to find out how many tasks are overdue
    #Only overdue tasks with the user_name at index[0] will be accounted for
    #Use for loop to count how many overdue tasks are assigned to the particular user
    import datetime
    today = datetime.datetime.today()
    with open("tasks.txt","r") as f:
        user_due_count = 0
        user_overdue_count = 0
        file = f.readlines()
        for line in file:
            line_list = file[user_due_count].strip().split(",")
            user_due_count+=1  
            if datetime.datetime.strptime(line_list[4],' %Y-%m-%d') < today and username in line_list[0]:
                user_overdue_count += 1          
        
    user_overview.write("\nOverdue Tasks for {}: {}".format(username, user_overdue_count))
    
    
    
    
    #Calculate percetange of tasks assigned to user that are overdue using simple math
    #Write results to file
    user_incomplete_percent = (todo_count/user_in_line_count)*100
    overdue_percent = (user_overdue_count/user_in_line_count)*100
    user_overview.write("\nPercentage of {}'s Tasks That Are Incomplete: {}".format(username, user_incomplete_percent))
    user_overview.write("\nPercentage of {}'s Tasks That Are Overdue: {}".format(username, overdue_percent))
    
    
    
    
    #Close file with all new information overwritten
    user_overview.close()
    
    #Open file again and print all the information for the user
    user_overview = open("user_overview.txt", "r")
    print ("\nUser Overview Report: \n")
    print (user_overview.read())
    user_overview.close()
    print("")


#Create funcion to generate both reports
#Use try except to let the program keep running if there is an indexing or date formatting error
def generate_reports():
    
    try:
        generate_task_overview()
        generate_user_overview()
    except:
        print("Task and User Overview: ")
        print("\nOops! There appears to be an error with the formatting of one or more tasks in tasks.txt")

        

    
import datetime

menu_choice = "a"
#Again indexing and .lower() was used to reduce user errors
#All information input by user was then saved to the tasks.txt file using .write()
#I could have used if statement instead of while loop but it still works and I was afraid to change anything once the program appeared to be working
def add_task():
    assign_to = input("Who is this task assigned to? (enter system username): ")
    assign_title = input("Create assignment title: ")
    assign_descript = input("Create assignment description: ")
    assign_date = datetime.datetime.now()
    due_date = input("Enter assignment due date (NB use yyyy-mm-dd format , do not use \ or /): ")
    assignemnt_complete = "No"
    write_to_file = (f"{assign_to}, {assign_title}, {assign_descript}, {assign_date}, {due_date}, {assignemnt_complete}")

    with open ("tasks.txt", "a") as tasks:
        tasks.write("\n"+write_to_file)
        print ("New task created!")
        print ("")
        print ("")




menu_choice = "va"
#https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python
#I used the resource above to find a way to make the information display a bit more readable for the user
#The for loop essentially goes through each line in the tasks.txt file and splits the information at every comma forming a list
#Then use indexing from the list and .format() to print the most important pieces of information in a way that is easy to read
def view_all():
    with open ("tasks.txt", "r") as tasks:
        print ("\nTASKLIST")
        for line in tasks:
            values = line.split(",")
            if len(values) >= 5:
                print ("\nTask Title: {}".format(values[1]))
                print ("Task Description: {}".format(values[2]))
                print ("due date:{}".format(values[4]))
                print ("Responsible user: {}".format(values[0]))
                print ("")
                print ("")




#Essentially repeat the exercise above except with the use of an if statement to make sure that only information relevant to the logged in user is displayed
#Start by creating a display for the user that shows only tasks relevant to them
#Declare variable task_num to number each task in the tasks.txt file for easy selection
menu_choice = "vm"
def view_mine():
    with open ("tasks.txt", "r") as tasks:
        print(f"\n{username}'s Tasks:")
        task_num = 0
        for line in tasks:
            task_num += 1
            if username in line:
                print ("\nTask Number: {}".format(task_num))
                print ("Task Title: {}".format(line.split(",")[1]))
                print ("Task Complete: {}".format(line.split(",")[5]))
                print ("due date:{}".format(line.split(",")[4]))
                print ("")
                print ("")
    
    
    
    
    #The tools for my solution to allow users to correct specific pieces of information came from a combination of the next two sources below
    #https://stackoverflow.com/questions/60971143/changing-the-correct-object-in-the-text-file         
    #https://www.youtube.com/watch?v=Y5EMGBo39Kk
    #Begin by allowing user to choose whether they want to edit any of their tasks or go back to main menu using input()
    edit = input("Would you like to edit a task? (edit) or return to the main menu? (-1)\n")
    
    
    #Use indexing and .lower() to minimize user based errors. I will be using this extensively throughout
    if edit[0].lower()== "e":
        
       
        #If user has chosen to edit the tasks we first allow them to select exactly which task they would like to take a closer look at
        #Use readlines() to turn the text in the file into a list of lines and then indexing to select the correct line with the task_num variable we delcared earlier
        task_num = int(input("Please enter the Task number of the task you would like to make changes to\n"))
        task_num = task_num -1
        with open('tasks.txt', 'r') as f:
            file = f.readlines()
            print(file[task_num] + "\n")
            
            
        #Once user has zoned in on the exact task they would like to edit (which, again, is simply a specific line within the tasks.txt file), give them and option to mark as complete or edit the task 
        edit_choice = input("Would you like to mark this task as complete ('mark') or edit the task ('edit')?: ")
        
        
        #If user chooses to mark as complete then there are several steps to be taken
        #The correct line must first be selected as before
        #Then that line is turned into a list of strings with .split()
        #Then the index of that list that contains the Yes/No regarding the completion of the task is selected and changed to "Yes"
        #Then the updated list is turned back into a string with .join() and inserted at the correct index in the list of lines
        #The entire file is then overwritten with the new information
        #Also print message for user to let them know that their changes have been made
        if edit_choice[0].lower() == "m":
            with open("tasks.txt","r") as f:
                file = f.readlines()
                line_list = file[task_num].strip().split(",")
                line_list[5] = " Yes\n"
                new_line = ",".join(line_list)
                file[task_num] = new_line
                print ("\nYour task has been marked complete")
                print (new_line)
                
            with open("tasks.txt", "w")as f:
                f.writelines(file)
            
                
        #If the user chooses to edit the task instead of just mark as complete the program will search for "Yes"/"No" at the last index on the line specified by the user choice
        #If there is a "Yes", this task is already complete and the user is notified that they cannot make changes
        #If there is a "No" then changes are made to the line based on the same principles as the code just above except now the changes are specified by the user with input()
        #Print message to user letting them know their changes have been made
        if edit_choice[0].lower() == "e":
            with open("tasks.txt","r") as f:
                file = f.readlines()
                line_list = file[task_num].strip().split(",")
                if "No" in line_list[5]:
                    line_list[0] = input("Who would you like to assign this task to?: ")
                    line_list[4] = " due date:" + input("New due date: ")
                    line_list[5] = line_list[5] + "\n"
                    new_line = ",".join(line_list)
                    file[task_num] = new_line
                    print ("\nYour task has been updated")
                    print (new_line)
                if "Yes" in line_list[5]:
                    print("\nSorry, this task is already complete and cannot be edited")
                
            with open("tasks.txt", "w")as f:
                f.writelines(file)




#Step 1, create a login requirement
#We begin by opening the user.txt file which has all the authorised users on it
#The user is prompted to enter a username and password to see the menu
#Use an if elif else statement to check and make sure the username and password are in the user.txt files
#Should the user enter an invalid username or password, they will be duly notified and the while loop will prompt them to continue trying
#The major weakness at this point is that the password does not necessarilly have to correpond to the username. Will figure this out later
with open("user.txt", "r") as users:
        users = users.read()
while True:
    username = input("Username: ")
    password = input("Password: ")
    if username in users and password in users:
        print ("Welcome\n")  
        break
    elif username not in users and password in users:
        print ("fail, username not correct")
        continue
    elif username in users and password not in users:
        print ("fail, password not correct")
        continue
    else:
        print ("fail, username and password not correct")
        continue




#Overarching while loop to run program after log in until user hits 'e'
while True:

    #Admin user is provided with a new menu option that allows them to view the program statistics
    #Use an if statement to pick up when a user named "admin" logs in and offer them the additional menu option before moving on to the main menu
    #Program will prompt admin user to enter 's' to see the stats or 'm' to move straight to the main menu. In reality, the user could enter any value to move straight to the main menu.
    if username == "admin": 
        admin_menu = input("Hey Admin! Enter 's' to view program stats or 'm' to move straigt to the main menu: ")


        #If the user is admin and selects 's' to see the stats. The task overview report and user overview report will display the information fromt the text file
        if admin_menu.lower() == "s":
            task_overview = open("task_overview.txt", "r")
            print ("\nTask Overview Report: \n")
            print(task_overview.read())
            task_overview.close
            user_overview = open("user_overview.txt", "r")
            print ("\nUser Overview Report: \n")
            print (user_overview.read())
            print ("")
            user_overview.close()
            



    #We move on to the main menu
    #Prompt user to select from a variety of options using input()
    menu_choice = input("Please select one of the following options: \nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \ne - exit \n ")


    #Use indxing and .lower() to avoid user errors from becoming a problem
    #If non user admin selects register they will be told they are not authorised to do so and the program ends
    while menu_choice[0].lower() == "r":
        if username != "admin":
            print ("\n*Sorry, you are not authorised to add a user*")
            break

        else:
            reg_user()
            break

        

  
    #If the user chose the assign a new task from the menu then they are prompted to provide all the necessarry information required to meet the format of the tasks.txt file
    if menu_choice[0].lower() == "a":
        add_task()
        


    
    #If the user chooses va, the program will display all the tasks in the database
    if menu_choice.lower() == "va":
        view_all()




    #If user chooses vm, program will display only tasks relevant to user who is logged in
    if menu_choice.lower() == "vm":
        view_mine()

    
    
    
    if menu_choice.lower() == "gr":
        generate_reports()
        
    
    
    
    #The easiest part of the project
    #Use if statement to end the program and print a goodbye message to the user should they enter 'e' at the main menu
    if menu_choice.lower() == "e":
        print ("\nThank you! Goodbye")
        break
              
            
            
            


