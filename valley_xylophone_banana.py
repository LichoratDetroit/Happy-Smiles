#Importing libraries
import pandas as pd 
from ipywidgets import widgets
import matplotlib.pyplot as plt
import seaborn as sns

#initializing variables
appointments = {}
date_time = ""
date_time_str = ""
timetime_str = ""
appt_type = ""
client_name = ""

#Creating functions
#Function to add an appointment
def createAppt(client_name, date_time, appt_type):
    if date_time not in appointments:
        appointments[date_time] = (client_name, appt_type)
    else:
        print("Date and time already taken")

#Function to delete an appointment
def deleteAppt(date_time):
    if date_time in appointments:
        del appointments[date_time]
    else:
        print("Date and time not found")

#Function to edit an appointment
def editAppt(client_name, date_time, appt_type):
    if date_time in appointments:
        appointments[date_time] = (client_name, appt_type)
    else:
        print("Date and time not found")

#Function to get data
def getData():
    date_time_list = [x for x in appointments]
    client_name_list = [appointments[x][0] for x in appointments]
    appt_type_list = [appointments[x][1] for x in appointments]
    df = pd.DataFrame(list(zip(date_time_list, client_name_list, appt_type_list)), 
               columns =['Date_Time','Name', 'Appointment_Type']) 
    return df

#Function to display the data
def displayData():
    df = getData()
    plt.figure(figsize=(15, 10))
    sns.set_style("darkgrid")
    sns.scatterplot(x="Date_Time", y="Name", hue="Appointment_Type", data=df)
    plt.show()

#Main function
def main():
    while(True):
        print("Welcome to The Dental Clinic Appointment Management")
        print("1. Create Appointment")
        print("2. Delete Appointment")
        print("3. Edit Appointment")
        print("4. Display Appointments")
        print("5. Exit")
        try:
            user_input = int(input("Enter a choice: "))
        except ValueError:
            print("Invalid input.Enter a numeric value")
            continue
        else:
            if user_input == 1:
                date_time = widgets.DatePicker(
                            description='Date and Time',
                            disabled=False
                        )
                display(date_time)
                date_time_str = str(date_time.value)
                time_str = str(date_time.value.time())
                date_time = date_time_str + ' ' + time_str
                client_name = input("Enter the name of the client: ")
                appt_type = input("Enter the type of appointment: ")
                createAppt(client_name, date_time, appt_type)
                print("Appointment created successfully")
            elif user_input == 2:
                date_time = widgets.DatePicker(
                            description='Date and Time',
                            disabled=False
                        )
                display(date_time)
                date_time_str = str(date_time.value)
                time_str = str(date_time.value.time())
                date_time = date_time_str + ' ' + time_str
                deleteAppt(date_time)
                print("Appointment deleted successfully")
            elif user_input == 3:
                date_time = widgets.DatePicker(
                            description='Date and Time',
                            disabled=False
                        )
                display(date_time)
                date_time_str = str(date_time.value)
                time_str = str(date_time.value.time())
                date_time = date_time_str + ' ' + time_str
                client_name = input("Enter the name of the client: ")
                appt_type = input("Enter the type of appointment: ")
                editAppt(client_name, date_time, appt_type)
                print("Appointment edited successfully")
            elif user_input == 4:
                displayData()
            elif user_input == 5:
                break
            else:
                print("Invalid input. Enter a valid option")
            print()

if __name__ == '__main__':
    main()