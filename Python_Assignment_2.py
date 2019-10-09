import time  # Allows me to use sleep to tell the program to wait a certain amount of seconds before executing the next line of code
import re  # Allows me to validate my user input by not allowing it to be characters if I only want digits

with open("Records.txt") as file:  # Opens the text file with all the records in it
    records = [line.strip() for line in file if not line.startswith("#")]  # Creates a list named Records and stores all the records ignoring any lines with a '#'

# Explanation for colouring text
# \033[ is the escape code and never changes
# 34m is the fore colour and it is equal to blue
# To return the text colour to normal use \033[39m


def main():
    print("\n\033[34m" + "Select from one of the options below:\n" + "\033[39m")  # Asks the user to select one of the options on the menu. "\033" is the escape code, it never changes"\033[34m" Adds the colour to the text and "\033[39m" resets the colour
    print("Enter '1' to print out the number of records"  # Tells the user what will happen if they select 1
          "\nEnter '2' to display a list of employees and their respective details"  # Tells the user what will happen if they select 2
          "\nEnter '3' to display the total salary bill"  # Tells the user what will happen if they select 3
          "\nEnter '4' to display a report showing the average salary based on the amount of employees"  # Tells the user what will happen if they select 4
          "\nEnter '5' to add a new employee to the list"  # Tells the user what will happen if they select 5
          "\nEnter '6' to display a report to show the amount of employees that are in each position type"  # Tells the user what will happen if they select 6
          "\nEnter '7' to display employees who earn a higher salary than the threshold"  # Tells the user what will happen if they select 7
          "\nEnter '8' to search for an existing record"  # Tells the user what will happen if they select 8
          "\nEnter '9' to exit the program\n")  # Tells the user what will happen if they select 9

    user_choice = input("\033[34m" + "Please enter the number of the option you would like use: " + "\033[39m")  # Asks the user to select what they would to do with the program from a selection of options

    if user_choice == "1":  # Checks to see if the user has entered '1', if the user enters '1' then the code inside this IF Statement will execute
        number_of_lines()  # Call the number_of_lines function

    elif user_choice == "2":  # Checks to see if the user has entered '2', if the user enters '2' then the code inside this IF Statement will execute
        list_of_employees()  # Calls the list_of_employees function

    elif user_choice == "3":  # Checks to see if the user has entered '3', if the user enters '3' then the code inside this IF Statement will execute
        print("\nYour salary total is £", format(total_salary(), ",.2f"), sep='')  # calls the total_salary function and separates it with a space
        total_salary_finished = input("\n\033[33m" + "Are you ready to return back to the menu?(yes/no): " + "\033[39m").lower()
        if total_salary_finished == "yes":  # Checks if the users input is equal to yes
            main()  # If users input it equal to yes then the user will be returned to the main function
        else:
            total_salary()  # If the user enters anything but yes then they will be returned to the total salary function

    elif user_choice == "4":  # Checks to see if the user has entered '4', if the user enters '4' then the code inside this IF Statement will execute
        average_salary()  # Calls the average_salary function

    elif user_choice == "5":  # Checks to see if the user has entered '5', if the user enters '5' then the code inside this IF Statement will execute
        add_new_employee()  # Calls the add_new_employee function

    elif user_choice == "6":  # Checks to see if the user has entered '6', if the user enters '6' then the code inside this IF Statement will execute
        number_of_position_type()  # Calls the number_of_position_type function

    elif user_choice == "7":  # Checks to see if the user has entered '7', if the user enters '7' then the code inside this IF Statement will execute
        above_salary_threshold()  # Calls the above_user_threshold function

    elif user_choice == "8":  # Checks to see if the user has entered '8', if the user enters '8' then the code inside this IF Statement will execute
        search_for_a_record()  # Calls the add_new_employee function

    elif user_choice == "9":  # Checks to see if the user has entered '9', if the user enters '9' then the code inside this IF Statement will execute
        print("\n\033[32m" + "Program closed successfully")  # Prints a message to the user and formats the text to green
        exit()  # Exits the program

    else:
        print("\n\033[31m" + "Enter a number between 1 to 9 " + "\033[39m")  # Displays a message to the user if they do not select one of the above options and formats the text colour to be red
        time.sleep(2)  # Waits 2 seconds before executing the next line of code
        main()  # Returns to the main function


# End of IF Statement


def number_of_lines():  # Creates a function named 'number_of_lines'
    records_count = sum(1 for records_count in open("Records.txt") if not records_count.startswith("#"))  # converts the record_count to a sum and calculates the number of lines in the records.txt file, ignoring the commented lines
    print("\nThe number of records is:", records_count)  # Prints the number of records for the user to see
    lines_finished = input("\n\033[33m" + "Are you ready to return back to the menu?(yes/no): " + "\033[39m").lower()  # Asks the user for input
    if lines_finished == 'yes':  # Checks the users input to see if it is 'yes' , if the users input matches the condition then the code inside the IF will run
        main()  # Returns the user to the main function
    else:
        number_of_lines()  # If the user types anything but yes then the number_of_lines function will run


def list_of_employees():  # Creates a function named 'list_of_employees'
    for line in open("Records.txt"):  # Opens the records text file
        if not line.startswith("#"):  # removes any lines that start with a '#'
            print(line.rstrip())  # prints the records to the user
    employees_finished = input("\n\033[33m" + "Are you ready to return back to the menu?(yes/no): " + "\033[39m").lower()
    if employees_finished == 'yes':  # Checks if the users input is equal to yes
        main()  # Returns the user to the main function
    else:
        list_of_employees()  # If the user types anything but yes then the list_of_employees function will run


def total_salary():  # Creates a function named 'total_salary'
    with open("Records.txt", "r") as record_file:  # Opens the records files as read and creates a variable called record_file
        salaries_list = (record_file.read().split()[11::7])  # Creates a variable named salaries_list, the records files is then read in and split. I then tell the program to start on index 11 and to skip the next 7 elements, this happens until the loop is over
        salaries = ' '.join(salaries_list)  # joins all values into a list
        salaries = salaries.replace(',', '')  # Replaces all the ',' with spaces
        salaries = salaries.split()  # Puts all the salaries into a list again
        total = 0  # creates a variable called total
        for i in salaries:  # Creates a for loop to loop the salaries and add them all together
            total += int(i)  # Increments by one every time adding all the salaries together
        return total  # returns the total value


def average_salary():  # Creates a function named 'average_salary'
    record_count = sum(1 for record in open("Records.txt") if not record.startswith("#"))  # converts the record_count to a sum and calculates the number of lines in the records.txt file
    print("\nThe amount of employees is:", record_count)  # Prints out the number of records and takes away one to take away the heading line inside the text file
    salary = total_salary()  # stores the total_salary() function inside a variable
    print("\nThe total salary is: £", format(salary, ",.2f"), sep='')  # Prints the total salary to the user
    print("\nThe average salary is: £", format(salary / record_count, ",.2f"), sep='')  # Takes the total salary bill and divides it by the amount of lines and formats it to 2 decimal places
    average_salary_finished = input("\n\033[33m" + "Are you ready to return back to the menu?(yes/no): " + "\033[39m").lower()  # Stores the users input into the average_salary_finished variable and converts it to lowercase
    if average_salary_finished == 'yes':  # Checks if the users input is equal to yes
        main()  # Returns the user to the main function
    else:
        average_salary()  # If the user types anything but yes then the average_salary function will run


def add_new_employee():  # Creates a function named 'add_new_employee'
    with open("records.txt", "a+") as storing_records:  # Opens the record text file for append+ so that anything written to the text file will be written to the end and also so I can read the file
        last_record = records[-1]  # Creates a variable called last_record and stores the values of the records variable inside, then it gets the last value in the list.
        print("\nThe last record in the file is:\n" + last_record, "\n" + "\nPlease enter the number that comes after the previous Employee ID")  # Prints the last_record variable
        another_record = "y"  # Creates a variable called another_Record and sets it to 'y'
        while another_record == "y" or another_record == "Y":  # Creates a while loop that will keep running as long as the another_Record variable is set to 'y' or 'Y'
            employee_number = input("\nEnter your employee number:")  # Stores the users input in the employee_number variable
            if len(employee_number) < 3 or len(employee_number) > 3:  # First checks to see if the employee number is 3 digits
                print("\n\033[31m" + "Employee number must be 3 digits" + "\033[39m")
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            elif not re.match("^[0-9]*$", employee_number):  # if the employee number is 3 digits then it then checks to see if it is a digit between 0 - 9
                print("\n\033[31m" + "Employee number must only contain digits from 0 - 9" + "\033[39m")
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            employee_name = input("\nEnter your name:")  # Stores the users input in the employee_name variable
            employee_age = input("\nEnter your age:")  # Stores the users input in the employee_age variable
            if not re.match("^[0-9]*$", employee_age):  # First checks to see if the inputted age is a digit between 0 - 9, if the user enters in anything that isn't 0-9 then the code inside the if statement will run
                print("\n\033[31m" + "Employee age must only contain digits from 0 - 9" + "\033[39m")  # Prints an error to the user
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            elif len(employee_age) > 3:  # If the employee age is between the 0 - 9 then it checks to see if the inputted age is greater than 3 digit, if the age is greater than 3 digits then the code inside the elif statement will run
                print("\n\033[31m" + "Employee age must less than 3 digits" + "\033[39m")  # Prints an error to the user
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            print("\n\t\033[34m" + "Positions" + "\033[39m"  # Prints a message to the user
                  "\nEnter '1' for Developer "
                  "\nEnter '2' for DevOps"
                  "\nEnter '3' for Analyst"
                  "\nEnter '4' for Tester"
                  "\nEnter '5' for Designer")
            user_choice = input("\n\033[34m" + "Enter the number of your position:" + "\033[39m")  # Stores the users input to the user_choice variable
            employee_position = ""  # Creates a variable and sets it to a blank string
            if user_choice == "1":  # Checks if the users input is equal to 1, if it is then the code inside this if statement will run, if not then it will check the next elif statement
                employee_position = "Developer"  # Sets the employee_position variable to 'Developer'
            elif user_choice == "2":  # Checks if the users input is equal to 2, if it is then the code inside this if statement will run, if not then it will check the next elif statement
                employee_position = "DevOps"  # Sets the employee_position variable to 'DevOps'
            elif user_choice == "3":  # Checks if the users input is equal to 3, if it is then the code inside this if statement will run, if not then it will check the next elif statement
                employee_position = "Analyst"  # Sets the employee_position variable to 'Analyst'
            elif user_choice == "4":  # Checks if the users input is equal to 4, if it is then the code inside this if statement will run, if not then it will check the next elif statement
                employee_position = "Tester"  # Sets the employee_position variable to 'Tester'
            elif user_choice == "5":  # Checks if the users input is equal to 5, if it is then the code inside this if statement will run, if not then it will check the next else statement
                employee_position = "Designer"  # Sets the employee_position variable to 'Designer'
            else:
                print("\n\033[31m" + "Choose a number between 1 and 5" + "\033[39m")  # Prints an error to the user
                time.sleep(3)
                add_new_employee()  # Returns to the add_new_employee function
            employee_salary = input("\nEnter your salary:")  # Stores the users input in the employee_salary variable
            if not re.match("^[0-9]*$", employee_salary):  # checks to see if the inputted salary is a digit between 0 - 9, if the user enters in anything that isn't 0-9 then the code inside the if statement will run
                print("\n\033[31m" + "Employee salary must be digits between 0 - 9" + "\033[39m")  # Prints an error to the user
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            employee_years = input("\nEnter the amount of years you have been employed:")  # Stores the users input in the employee_years variable
            if not re.match("^[0-9]*$", employee_years):  # checks to see if the inputted years employed is a digit between 0 - 9, if the user enters in anything that isn't a digit between 0-9 then the code inside the if statement will run
                print("\n\033[31m" + "Employee years must only contain digits between 0 - 9" + "\033[39m")  # Prints an error to the user
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            elif len(employee_years) > 2:  # If the employee years is between the 0 - 9 then it checks to see if the inputted years is greater than 2 digit, if the years is greater than 3 digits then the code inside the elif statement will run
                print("\n\033[31m" + "Employee years must be not be more than 2 digits" + "\033[39m")  # Prints an error to the user
                time.sleep(3)  # Waits 3 seconds before executing the next line of code
                add_new_employee()  # Returns the the top of the add_new_employee function
            user_input_record = employee_number + ', ' + employee_name + ', ' + employee_age + ', ' + employee_position + ', ' + employee_salary + ', ' + employee_years  # Adds all the user inputs together and separates them with comas
            storing_records.write(user_input_record + "\n")  # Stores the user input in the records text file
            another_record = input("\n\033[33m" + "Do you want to input another record? (yes/no): " + "\033[39m").lower()  # Asks the user if they want to add another record, if the user types 'y' or 'Y' then the while loops will run again
    if another_record == 'yes':  # Checks if the another_record variable is set to 'yes', if it is then the code inside the if statement will run
        add_new_employee()  # If the user types anything but yes then the add_new_employee function will run
    else:
        main()  # Returns the user to the main function


def number_of_position_type():  # Creates a function called number_of_position_type
    with open("Records.txt", "r") as record:  # Reads in the text file as record
        position_type_list = (record.read().split()[10::7])  # Creates a variable named position_type_list, the records files is then read in and split. I then tell the program to start on index 10 and to skip the next 7 elements, this happens until the loop is over
        position_type = ' '.join(position_type_list)  # joins all values into a list
        position_type = (position_type.replace(',', ''))  # Replaces all the ',' with spaces
        developer = position_type.count("Developer")  # Creates a variable called developer and counts the position_type variable to see how many times the word 'Developers' appears
        print('%-40s%-0s' % ("The total number of Developers is:", developer))  # Prints out the developer variable
        devops = position_type.count("DevOps")  # Creates a variable called devops and counts the position_type variable to see how many times the word 'DevOps' appears
        print('%-40s%-0s' % ("The total number of DevOps is:", devops))  # Prints out the devops variable
        analyst = position_type.count("Analyst")  # Creates a variable called analyst and counts the position_type variable to see how many times the word 'Analyst' appears
        print('%-40s%-0s' % ("The total number of Analysts is:", analyst))  # Prints out the analyst variable
        tester = position_type.count("Tester")  # Creates a variable called analyst and counts the position_type variable to see how many times the word 'Tester' appears
        print('%-40s%-0s' % ("The total number of Testers is:", tester))  # Prints out the tester variable
        designer = position_type.count("Designer")  # Creates a variable called designer and counts the position_type variable to see how many times the word 'Designer' appears
        print('%-40s%-0s' % ("The total number of Designers is:", designer))  # Prints out the designer variable
    position_finished = input("\n\033[33m" + "Are you ready to return back to the menu?(yes/no): " + "\033[39m").lower()  # Stores the user input into the position_finished variable
    if position_finished == 'yes':  # Checks the users input to see if it equal to 'yes'
        main()  # Returns the user to the main function
    else:
        number_of_position_type()  # Returns the user to the search_for_a_record function


def above_salary_threshold():  # Creates a function called above_salary_threshold
    try:  # Tries the code for any errors
        user_threshold = int(input("\nEnter the salary threshold: "))  # Asks the user to input data and stores it as an integer
        for line in records:  # Creates a for loop
            columns = line.split(', ')  # Creates a variable called fields and splits the lines that have ','
            if user_threshold <= int(columns[4]):  # Creates an if statement
                print('%03i\t\t%-20s£%-10.2f' % (int(columns[0]), columns[1], int(columns[4])))  # Formats the output
        above_salary_finished = input("\n\033[33m" + "Are you ready to return back to the menu?(yes/no): " + "\033[39m").lower()
        if above_salary_finished == 'yes':  # Checks if the users input is equal to yes
            main()  # Returns the user to the main function
        else:
            above_salary_threshold()  # Returns the user to the above_salary_threshold function
    except ValueError:  # Catches any value errors
        print("\n\033[31m" + "You have entered an invalid number" + "\033[39m")  # Prints a message to the user
        time.sleep(2)  # Waits 2 seconds before going to the above_salary_threshold function
        above_salary_threshold()  # goes to the above_Salary_threshold function


def search_for_a_record():
    try:  # Tries the code for any errors
        data = open('Records.txt').read().splitlines()  # opens the records file and reads and splits the lines and stores it to the data variable
        emp_no = input("\n\033[34m" + "Enter the UserID you would like to search for: " + "\033[39m")  # Creates a variable called emp_no and asks the user to enter a userID
        record = [line for line in data if line.split(',')[0] == emp_no][0]  # Creates a for loop to search through the list of records and splits them up and searches each line for the value entered in by the user
        print(record)  # Prints the records variable
        another_record = input("\n\033[33m" + "Do you want to enter another User_ID?(yes/no): " + "\033[39m").lower()  # Stores the user input as lowercase
        if another_record == 'yes':  # Creates an IF statement to see if the user wants to search for another record, if the user selects yes the code in this section will run
            search_for_a_record()  # Returns to the beginning of the search_for_a_record function
        else:
            main()  # Returns the user to the main function
    except IndexError:  # Catches any errors
        print("\n\033[31m" + "You have entered an invalid number" + "\033[39m")  # Prints a message to the user
        search_for_a_record()  # Returns the user to the search_for_a_record function


users_name = input("What is your name?: ")  # Asks the user for their name and stores their input to the users_name variable
print("\nWelcome", users_name)  # Prints welcome followed by the name stored in the users_name variable

main()  # calls the main function
