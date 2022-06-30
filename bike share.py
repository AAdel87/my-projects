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
    while True:
        city = input("\nWhich city would choose to sort? 'chicago', 'new york city', 'washington'?\n").strip().lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("sorry, please choose the correct city name")
            continue
        else:
            break
        
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
  
    while True:
        month = input("\nwhich month would you choose to sort? january, february, march, april, may, june or type 'all' ?\n").strip().lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("sorry, please choose the correct month name. try again.")
            continue
        else:
            break
                         
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
            day = input("\nwhat day's would you choose to sort?: saturday, sunday, monday, tuesday, wednesday, thursday, friday, or 'all'.\n").strip().lower()
            if day not in ('saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all'):
                print("sorry, please choose the correct day's name.")
                continue
            else:
                break
                

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['start time'] = pd.to_datetime(df['start time'])
    df['month'] = df['start time'].dt.month
    df['day of week'] = df['start time'].dt.weekday_name
    df['hour'] = df['start time'].dt.hour
    if month != 'all':
               months = ['january', 'february', 'march', 'april', 'may', 'june']
               month = months.index(month) + 1
               df = df[df['month'] == month]
    if day != 'all':
                df = df[df['day_of_week'] == day.title()]
                                          
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popularmonth = df['month'].mode()[0]
    print('most common month:', popularmonth)

    # TO DO: display the most common day of week

    popularday = df['day of week'].mode()[0]
    print('most common day:', popularday)
    

    # TO DO: display the most common start hour

    df['hour'] = df['start time'].dt.hour
    popularhour = df['hour'].mode()[0]
    print('most common hour:', popularhour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startstation = df['start station'].value_counts().idxmax()
    print('most commonly used start station:', startstation)

    # TO DO: display most commonly used end station

    endstation = df['end station'].value_counts().idxmax()
    print('\n most commonly used and station:', endstation)
    

    # TO DO: display most frequent combination of start station and end station trip

    frequentstation = df.groupby(['start station', 'end station'])
    mostfrequentstation = frequentstation.size().sort_value(ascending=False).head(1)
    print('\nmost frequent combination of start station and end station trip:', mostfrequentstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    totaltraveltime = df['trip duration'].sum()
    print('total travel time:', totaltraveltime, "minutes")
    meantraveltime = df['trip duration'].mean
    print('mean travel time is: ', meantraveltime, "minutes")
    

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
      
    usertypes = df['user type'].value_counts()
    print('user types:\n', usertypes) 

    # TO DO: Display counts of gender
    try:
        gendertypes = df['gender'].value_counts()
        print('\ngender types:\n', gendertypes)
    except KeyError:
        print("\ngender types:\nsorry, there's no data for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliestyear = df["birth year"].min()
        print('\nearliest year:\n', earliestyear)
    except KeyError:
        print("\nearliest year:\nsorry, there's no data for this month.")
    try:
        mostrecentyear = df["birth year"].max()
        print('\nmost recent year:', mostrecentyear)
    except KeyError:
        print("\nmost recent year:\nsorry, ther's no data for this month.")
    try:
        mostcommonyear = df["birth year"].mode(0)
        print('\nmost common year:', mostcommonyear)
    except KeyError:
        print("\nmost common year:\nsorry, there's no data for this month.")
                                 
def showerowdata(df):
    row=0
    while True:
        viewrowdata = input("do you like to see the raw data? 'yes' or 'no'.").lower
        if viewrowdata == "yes":
            print(df.iloc[row : row + 6])
            row += 6
        elif viewrowdata == "no":
            break
        else:
            print ("sorry, 'yes' or 'no'")                
                            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        showerowdata(df)           

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
