# Task-Managment-Program

## Project Detials

### Description:
In this task, I was to create a program for a small business to help it to manage tasks assigned to each member of the team. This program works with two text files, user.txt and tasks.txt. tasks.txt stores a list of all the tasks that the team is working on. Each line includes the following data about a task in this order:

1. The username of the person to whom the task is assigned.
2. The title of the task.
3. A description of the task.
4. The date that the task was assigned to the user.
5. The due date for the task.
6. Either a ‘Yes’ or 'No’ value that specifies if the task has been completed yet

It is important that each data point is seperated by a comma and one space and that the dates are written in the correct YYY-MM-DD format e.g:

    bob, task1, do the task, 2021-01-01, 2021-01-30, No

user.txt stores the username and password for each user with the username and password also being seperate by a comma and one space and only one username and corresponding password per line, e.g:

    bob, HUnter67
    

### Functionality:
The user is first asked to login by entering their username and password. If their password or username is not correct, they are alerted by an error message and prompted to try again until a valid username password combination has been entered by the user. After a successful login, the following options are given in the main menu:

1. r - register user
2. a - add task
3. va - view all tasks
4. vm - view my tasks'
5. gr - generate reports
7. e - exit

Only if the user is logged in as admin can they register a new user. The Admin user is also given the option to view all the program statistics before the main menu is displayed.

If user selects add task, they are prompted to enter the information needed to store the task as a line in the task.txt file in the order previously mentioned above. The task is automatically saved with the last data as a "No" marking it as incomplete.

If the user enters 'va' for view all, all the tasks in the task manager are displayed in a user friendly format that summarises the details of each task individually

If the user enters 'vm', all the tasks assigned to them only will be displayed, as well as a sub menu with additional options to either edit one of their tasks, mark a task as complete or return to the main menu. If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that describes whether the task has been completed or not is changed to ‘Yes’. When the user chooses to edit a task, the username of the person to whom the task is assigned or the due date of the task can be edited. The task can only be edited if it has not yet been completed.

If the user enters 'gr', to generate reports, two text files, called task_overview.txt and user_overview.txt, are generated.
task_overview.txt will display the following:
1. The total number of tasks
2. The total number of completed tasks
3. The total number of uncompleted tasks
4. The total number of tasks that are overdue
5. The percentage of tasks that are incomplete
6. The percentage of tasks that are overdue

user_overview.txt will display the following:
1. The total number of users registered in the task manager
2. The total number of tasks 
3. The total number of tasks assigned to the user 
4. Percentage of the total number of tasks that have been assigned to that user
5. Percentage of the tasks assigned to that user have been completed
6. Percentage of the tasks assigned to that user still to be completed
7. Percentage of the tasks assigned to that user that are overdue


### Usefulness:
This Python project is useful because it shows the beginning stages of what can be a successful task management system for a small company.
