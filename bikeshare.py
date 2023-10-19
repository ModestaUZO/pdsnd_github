import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.
  
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWelcome to this program. Please enter a city name:")
        print("\n1. Chicago 2. New York City 3. Washington")
        print("/nValid input:\nFull city name: not case sensitive(e.g. WAShingToN or washington).\nFull name in title case(e.g. Washington).")
        #Now i would take user inputs and convert into lower
        city = input().lower()
        
        if city not in CITY_DATA.keys():
            print("\nI can't seem to find your input here, please try again!")
            print("\nLoading...")
            
    print("You have chosen {} to analyse.".format(city.title()))
      


    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6, 'all' : 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("Please enter a month between January to June:")
        print("/nValid input:\nFull month name: not case sensitive(e.g. MArch or march).\nFull month name in title case(e.g. March).")
        print("You may also want to view the data for all the months given, please type 'all' or 'All' or 'ALL'.")
        #Again, I would take user inputs and convert to lower
        month = input().lower()
        
        if month not in MONTH_DATA.keys():
            print("\nI can't seem to find your input here, please try again!")
            print("\nLoading...")
            
    print("You have chosen {} to analyse.".format(month.title()))
  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday', 'sunday', 'all'] 
    day = ''
    while day not in DAY_DATA:
        print("\nPlease input a day of the week for which you'd llke to analyse:")
        print("/nValid input:\nFull day of the week name: not case sensitive(e.g. TUesday or tuesday).\nFull day name in title case(e.g. Tuesday).")
        print("You may also want to view the data for all the days of the week, please type 'all' or 'All' or 'ALL'.")
         
        #Again, I would take user inputs and convert to lower
        day = input().lower()
        
        if day not in DAY_DATA:
            print("\nI can't seem to find your input here, please try again!")
            print("\nLoading...")
            
    print("You have chosen {} to analyse.".format(day.title()))
    print("You have chosen to view data for city: {}, month(s): {} and day(s): {}.".format(city.upper(), month.upper(), day.upper()))
          
     #Return the city, month and day selection
    return city, month, day
  

#loading the data from .csv file
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
  # first of all, i would load the file into a dataframe
    df = pd.read_csv(CITY_DATA[city]) 
                     
  # Also, I would convert the start time column to datetime using the "to_datetime" function
    df['Start Time'] = pd.to_datetime(df['Start Time'])     
                     
   # Extracting the days and months from the 'Start Time' column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
                     
    # Next thing i would do is to filter by month
    # If applicable
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    # create a new dataframe by filtering by month
        df = df[df['month'] == month]           
                     
    # Next thing i would do is to filter by day of the week
     # If applicable
    if day != 'all':         
             #create a new dataframe by filtering by day of the week
       df = df[df['day_of_week'] == day.title()]            
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is: ", popular_month)
                     
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]           
    print("The most popular day is: ", popular_day)

    # TO DO: display the most common start hour
    # first things first, extract hour from the start time
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print("The most popular Start Hour is {}:00 hrs".format(popular_hour))
                     
                  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular Start Station is: ", popular_start_station)
                     
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular End Station is: ", popular_end_station)
    
    #display the combination of start and end station
    df['Start to End'] = df['Start Station'] + " "+"to"+" "+df['End Station']
    popular_combo = df['Start to End'].mode()[0]
    print("The most frequent combination of trips are from {} ".format(popular_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)                  
    print(f"The total travel time is {hour} hour(s) {minute} minute(s) {second} second(s)")
                     
    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    m, sec= divmod(average_duration, 60)
    if m > 60:                 
        h, m = divmod(m, 60)                  
        print("The average travel time is {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("The average travel time is {} minute(s) {} second(s)".format(m,sec))      
                     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print("The User Types with the total value counts:\n", user_count)                

    # TO DO: Display counts of gender
   # i used "try" to display the count of gender for all users but not all df have the gener column...
    try:
    except KeyError:
        print("Gender information is not available for this dataset.")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    #Likewise, I would "try" method
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())     
        common_year = int(df['Birth Year'].mode()[0])     
        print("\nThe earliest birth year is {}, \nThe most recent birth year is {}, \nThe most common birth year is {}".format(earliest_year, recent_year, common_year))    
    except:
        print("There are no details about birth year in this dataframe")
              
             
  
        
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
              
   # checking if the user wants to see more data  
def ask_more_data(df):
     """Displays extra 5 rows of data from the csv file if the user requests"""
     response = ['yes', 'no']
     more_data = ''
     counter = 0 
     while more_data not in response:
        print("\nDo you wish to view more rows of data?")
        print("Valid input:\nYes or yes\nNo or no")
        more_data = input().lower() 
            

       #the raw data is displayed if the users ask for it 
        if more_data == "yes":
            print(df.head())
        elif more_data not in response:
            print("\nPlease check your input.")
            print("Input doesn't seem to match any accepted responses.")
            print("\nLoading...\n")
          
          #a while loop to continue viewing data based on user's request
     while more_data == 'yes':
        print("Do you wish to view more data?")
        counter += 5
        more_data = input().lower()
          
          #if user chooses yes, it displays 5 more rows of data
        if more_data == 'yes':
            print(df[counter:counter+5])
        elif more_data != "yes":
            break
            
     print('-'*40)
          
          
               
          
          
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_more_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main() 


