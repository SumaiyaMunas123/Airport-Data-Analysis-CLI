"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w21577976/1 , 20242168
 4. Date: 2025/09/08
****************************************************************************

"""
from graphics import *
import csv
import math

data_list = []   # data_list An empty list to load and hold data from csv file

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name - set by the var 'selected_data_file' into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)


"""
EDIT THE CODE BELOW TO COMPLETE YOUR SUBMISSION
"""

#task A - user input function to validate and return user inputs for city code and year

#dictionary to map airport codes to full names
airport_names= {
    "LHR": "London Heathrow",
    "MAD": "Madrid Adolfo Suárez-Barajas",
    "CDG": "Charles De Gaulle International",
    "IST": "Istanbul Airport International",
    "AMS": "Amsterdam Schiphol",
    "LIS": "Lisbon Portela",
    "FRA": "Frankfurt Main",
    "FCO": "Rome Fiumicino",
    "MUC": "Munich International",
    "BCN": "Barcelona International"
}

def user_input():
    """
    This function gets and validates user input for the three letter city code and the four digit year
    It returns the validated city code and year so they can be used later
    """
    
    #getting three letter code for departure city and validating it
    
    valid_city_codes=["LHR","MAD","CDG","IST","AMS","LIS","FRA","FCO","MUC","BCN"]

    while True:
        city_code=input("\nPlease enter the three letter code for the departure city required: ").upper()
        if city_code.isdigit():#checking if the input is a digit
            print("Wrong data type - please enter a three letter city code")
        elif len(city_code)!=3:#checking if the input length is 3
            print("Wrong code length - please enter a three letter city code")
        elif city_code not in valid_city_codes:#checking if the input is in the list of valid city codes
            print("Unavailable city code - please enter a valid city code")
        else:
            break

    #getting required year in YYYY format    
    while True:
        year=input("\nPlease enter the year required in the format YYYY from a valid year between 2000 and 2025: ")
        if not year.isdigit():#checking if the input is a digit
            print("Wrong data type - please enter a four digit year value") 
        elif len(year)!=4:#checking if the input length is 4
            print("Wrong code length - please enter a four digit year value")
        elif int(year)>2025 or int(year)<2000:#checking if the input is in the valid range
            print("Out of range - please enter a value from 2000 to 2025")
        else:
            break

    return city_code,year#returning the validated inputs so they can be used later


#task B - extracting specific information from selected csv file

def calculate_outcomes(city_code,year,airport_names):
    """
    This function calculates and returns the required outcomes from the selected csv file
    It takes the city code, year and airport names dictionary as parameters so they can be used in the function
    """

    total_flights=len(data_list) #counts number of rows which is equal to the total number of flights from the airport
    runaway1_flights=sum(1 for row in data_list if row[8]=="1") #counts the total number of flights departing from that specific runaway
    over_500=sum(1 for row in data_list if int(row[5])>500) #counts the total number of departures of flights that travel distance over 500 miles
    BA_flights=sum(1 for row in data_list if row[1].upper().startswith('BA'))#counts the total number of British Airways flights from that airport
    rain_departures=sum(1 for row in data_list if 'rain' in row[9].lower())#counts the total number of flights departing in rain
    hourly_avg_flights=round(total_flights/12,2)#calculates the average number of flights per hour from that airport
    AF_flights=sum(1 for row in data_list if row[1].upper().startswith('AF'))#counts the total number of Air France flights from that airport
    AF_percentage=round((AF_flights/total_flights)*100,2)#calculates the percentage of Air France flights from that airport
    delayed_flights=sum(1 for row in data_list if row[2]!=row[3])#counts the total number of delayed flights from that airport
    delayed_percentage=round((delayed_flights/total_flights)*100,2)#calculates the percentage of delayed flights from that airport
    #calculates the number of unique hours in which rain fell
    unique_hours=set()
    for row in data_list:
        if 'rain' in row[9].lower():#checking column 10 , if rain is mentioned, without case sensitivity
            hour=int(row[3].split(":")[0])#extracting the hour from the scheduled departure time in column 4 by splitting and getting the first part
            unique_hours.add(hour)#adding the hour to a set to get unique hours
    rain_hours=len(unique_hours)
    #finding the most common destination(s) from that airport
    destination_count={}#dictionary to store the count of each destination
    for row in data_list:
        destination=row[4]#getting the destination from column 5
        if destination in destination_count:#updating the count if destination already exists in the dictionary
            destination_count[destination]+=1
        else:
            destination_count[destination]=1#initializing the count if destination does not exist in the dictionary
    max_count=max(destination_count.values())#finding the maximum count of destinations
    most_common_destination=[destination for destination , count in destination_count.items() if count==max_count]#getting all destinations with the maximum count
    long_name=[airport_names[destination] for destination in most_common_destination]#getting the full names of the most common destinations

    #storing all the outcomes in a dictionary
    outcomes={
        "city_code":city_code,
        "year":year,
        "total_flights":total_flights,
        "runaway1_flights":runaway1_flights,
        "over_500":over_500,
        "BA_flights":BA_flights,
        "rain_departures":rain_departures,
        "hourly_avg_flights":hourly_avg_flights,
        "AF_percentage":AF_percentage,
        "delayed_percentage":delayed_percentage,
        "rain_hours":rain_hours,
        "most_common_destinations":long_name
    }
    return outcomes#returning the dictionary of outcomes so they can be used later

def print_results(city_code,year,airport_names,outcomes):
    """
    This function prints the required outcomes to the screen
    It takes the city code, year, airport names dictionary and outcomes dictionary as parameters so they can be used in the function
    """

    #printing the results to the screen
    
    print("\n*********************************************************************************\n")
    print(f'File {outcomes["city_code"]}{outcomes["year"]}.csv selected - Planes departing {airport_names[city_code]} airport {year}\n')
    print("*********************************************************************************\n")

    print(f'The total number of flights from this airport was {outcomes["total_flights"]}\n')
    print(f'The total number of flights departing Runway 1 was {outcomes["runaway1_flights"]}\n')
    print(f'The total number of departures of flights over 500 miles was {outcomes["over_500"]}\n')
    print(f'There were {outcomes["BA_flights"]} British Airways flights from this airport \n')
    print(f'There were {outcomes["rain_departures"]} flights from this airport departing in rain \n')
    print(f'There was an average of {outcomes["hourly_avg_flights"]} flights per hour from this airport \n')
    print(f'Air France planes made up {outcomes["AF_percentage"]}% of all departures \n')
    print(f'{outcomes["delayed_percentage"]}% of all departures were delayed \n')
    print(f'There were {outcomes["rain_hours"]} hours in which rain fell \n')
    print(f'The most common destinations are {outcomes["most_common_destinations"]}\n')

#task c - saving the results to a file

def save_results(city_code,year,airport_names,outcomes):
    """
    This function saves the required outcomes to a text file
    It takes the city code, year, airport names dictionary and outcomes dictionary as parameters so they can be used in the function
    """

    #appending the results to a text file
    with open("results.txt", "a")as file:#opening the file in append mode so that previous results are not overwritten and new results are added at the end
        file.write("*********************************************************************************")
        file.write(f'File {outcomes["city_code"]}{outcomes["year"]}.csv selected - Planes departing {airport_names[city_code]} {year}')
        file.write("*********************************************************************************")

        file.write(f'The total number of flights from this airport was {outcomes["total_flights"]}\n')
        file.write(f'The total number of flights departing Runway 1 was {outcomes["runaway1_flights"]}\n')
        file.write(f'The total number of departures of flights over 500 miles was {outcomes["over_500"]}\n')
        file.write(f'There were {outcomes["BA_flights"]} British Airways flights from this airport \n')
        file.write(f'There were {outcomes["rain_departures"]} flights from this airport departing in rain \n')
        file.write(f'There was an average of {outcomes["hourly_avg_flights"]} flights per hour from this airport \n')
        file.write(f'Air France planes made up {outcomes["AF_percentage"]} of all departures \n')
        file.write(f'{outcomes["delayed_percentage"]} of all departures were delayed \n')
        file.write(f'There were {outcomes["rain_hours"]} hours in which rain fell \n')
        file.write(f'The most common destinations are {outcomes["most_common_destinations"]}\n')

        

#task D- Histogram

def histogram(city_code,year,airport_names,outcomes):
    """
    This function creates and displays a histogram of the number of flights departing each hour from 00:00 to 11:59 for a specific airline selected by the user
    It takes the city code, year, airport names dictionary and outcomes dictionary as parameters so they can be used in the function
    """

    #dictionary to map airline codes to full names
    airline_names = {
        "BA": "British Airways",
        "AF": "Air France",
        "LH": "Lufthansa",
        "KL": "KLM",
        "IB": "Iberia",
        "U2": "EasyJet",
        "FR": "Ryanair",
        "TK": "Turkish Airlines",
        "W6": "Wizz Air",
        "SN": "Brussels Airlines",
        "AY": "Finnair",
        "SK": "Scandinavian Airlines",
        "TP": "TAP Portugal",
        "EK": "Emirates",
        "QR": "Qatar Airways",
        "A3": "Aegean Airlines"
    }

    #getting airline code to plot histogram and validating it

    while True:
        airline_code=input("\nEnter a two character Airline code to plot a histogram: ").upper()
        if airline_code.isdigit():#checking if the input is a digit
            print("wrong data type- enter a two character airline code")
        elif len(airline_code)!=2:#checking if the input length is 2
            print("Enter the two character Airline code to plot a histogram")
        elif airline_code not in airline_names:#checking if the input is in the list of valid airline codes
            print("Unavailable Airline code please try again")
        else:
            break
        
    #getting no of flights per hour to draw histogram
    
    hourly_counts= [0] * 12 #list to hold counts of flights for each hour from 0 to 11
    for row in data_list:
        if row[1].startswith(airline_code):  #accessing column 2 for airline code
            hour = int(row[3].split(":")[0])  #accessing column 4 for scheduled departure time and extracting the hour
            if 0 <= hour < 12:  # only consider hours from 0 to 11
                hourly_counts[hour] += 1#incrementing the count for that hour

    #finding the maximum no of flights in any hour to set y axis limit
    max_flights= max(hourly_counts) if max(hourly_counts) > 0 else 1 #ensuring max_flights is at least 1 to avoid zero height graph

    #creating the window
    window=GraphWin("Histogram",1000,600)#setting the window size and title
    window.setBackground("lightyellow")#setting the background color
    window.setCoords(-1,-3,13,max_flights+5)#setting the coordinates for the window

    #drawing x axis
    Line(Point(0,0),Point(12,0)).draw(window)

    #drawing bars
    for hours in range(0,12):#iterating through each hour from 0 to 11
        gap=0.2#gap between bars
        bar=Rectangle(Point(hours+gap,0),Point(hours+1-gap,hourly_counts[hours]))#drawing each bar with a small gap on either side
        bar.setFill("lightcoral")#setting the fill color for the bars
        bar.setOutline("black")#setting the outline color for the bars
        bar.draw(window)#drawing the bar in the window

        #adding no of flights per hour count above each bar
        label=Text(Point(hours+0.5,hourly_counts[hours]+0.3),str(hourly_counts[hours]))#positioning the label above the bar
        label.setSize(12)#setting the font size for the label
        label.draw(window)

        #adding the hour under each bar
        hour_label=Text(Point(hours+0.5,-0.3),str(hours))#positioning the hour label under the bar
        hour_label.setSize(12)
        hour_label.draw(window)

    #adding title
    title=Text(Point(10,max_flights+3),f"Departures by hour for {airline_names[airline_code]} from {airport_names[city_code]} airport {year}")#setting the title with airline and airport names
    title.setSize(16)
    title.setStyle("bold")
    title.draw(window)

    #adding x axis label
    label2=Text(Point(6,-1),"Hours 00:00 to 12:00")
    label2.setSize(12)
    label2.setStyle("italic")
    label2.draw(window)

    #adding a message to click to close the window
    message = Text(Point(6, -2), "Click anywhere to close")#adding a message
    message.setSize(10)
    message.draw(window)
    
    window.getMouse()  #pause for click in window
    window.close()# Close window when done

#task E

def main():
    """
    This is the main program loop that integrates all tasks
    It repeatedly asks the user for a city code and year, loads the corresponding csv file, calculates outcomes, prints and saves results, and displays a histogram
    The loop continues until the user decides to exit
    """

    while True:
        city_code,year=user_input()#task A
        data_list.clear()#clearing the data list before loading a new file
        selected_data_file=f"{city_code}{year}.csv"
        #loading the selected csv file and handling file not found error
        try:
            load_csv(selected_data_file)
        except:
            print("\nNo such file found!")
            continue #asking user to input again if file not found

        airport_code= city_code.upper()#getting the airport code in uppercase using the city code
        airport_full_name= airport_names.get(airport_code)#getting the full name of the airport using the airport code

        outcomes=calculate_outcomes(city_code,year,airport_names)#task B
        print_results(airport_code,year, airport_names, outcomes)#task B
        save_results(airport_code,year, airport_names, outcomes)#task C
        histogram(airport_code,year, airport_names,  outcomes)#task D

        #asking user if they want to select a new data file
        continuity=input("\nDo you want to select a new data file? Y/N: ").lower()
        while (continuity not in ["y","n"]): #checking for valid input
            continuity=input("invalid input! Do you want to select a new file? y/n: ")
        if continuity=='n':
            print("\nThank you. End of run\n\n")
            break #exiting the loop if user does not want to continue
        elif continuity=='y':
            continue #asking for new input if user wants to continue
    
if __name__ == "__main__": #running the main program loop
    main()


"""#-----------------------------------------------------------------------------------------------------------------
#Some Example code queries to be replaced with those required by the brief - compare these outputs to the CSV file

first_row = data_list[0] #asign the list from the first row of the CSV to the var 'first_row'
second_item_in_secrow = data_list[1][1] #asign the second item (the flight number) from the second row of the CSV to a variable
third_item_in_thirdrow = data_list[2][2] #asign the third item (sheduled departure time) from the third row of the CSV to a variable

#PRINT THE OuTPUT TO SCREEN
print (f"The current file name is {selected_data_file}")
print ("")
print (f"First row of data_list is data_list[0] -> {first_row}")
print ("")
print (f"Second item of the second row is data_list[1][1] -> {second_item_in_secrow}")
print ("")
print (f"Third item of the third row is data_list[2][2] -> {third_item_in_thirdrow}")"""








