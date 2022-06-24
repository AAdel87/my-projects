from calendar import day_name, month, month_name
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
      city = input("\nWhich city would you choose to sort? 'new york city', 'chicago' or 'washington'?\n").strip().lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Sorry, please choose the correct city name")
        continue
      else:
        break


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

      month = input("\nWhich month would you choose to sort? January, February, March, April, May, June or type 'all' ?\n").strip()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Sorry, please choose the correct month name. Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      day = input("\nWhat day's would you choose to sort?: Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or 'all'.\n").strip()
      if day not in ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','all'):
        print("Sorry, please choose the correct day's name.")
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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common month

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common day of week
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltime = 60*60*24
    totaltraveltime = df['Trip Duration'].sum()
    print('The total travel time:', totaltraveltime/totaltime, " Days")

    # TO DO: display mean travel time
    meantime = 60
    meantraveltime = df['Trip Duration'].mean()
    print('Mean travel time:', meantraveltime/meantime, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes = df['User Type'].value_counts()
    print('User Types:\n', usertypes)
    # TO DO: Display counts of gender
    try:
      gendertypes = df['Gender'].value_counts()
      print('\ngender types:\n', gendertypes)
    except KeyError:
      print("\ngender types:\nsorry, there's No data for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      earliestyear = df['Birth Year'].min()
      print('\nEarliest Year:', earliestyear)
    except KeyError:
      print("\nEarliest Year:\nsorry, there's No data for this month.")

    try:
      mostrecentyear = df['Birth Year'].max()
      print('\nMost Recent Year:', mostrecentyear)
    except KeyError:
      print("\nMost Recent Year:\nsorry, there's No data for this month.")

    try:
      mostcommonyear = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', mostcommonyear)
    except KeyError:
      print("\nMost Common Year:\nsorry, there's No data for this month.")


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


