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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('\nHello! Let\'s explore some US bikeshare data. You can choose from Chicago, New York City, or Washington: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Incorrect input - please choose from Chicago, New York City or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Please choose a month between January and June: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Incorrect input - please choose a month between January and June: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Please choose a day of the week: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
       day = input("Incorrect input - please choose a day of the week between Sunday and Saturday: ").lower()

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

    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # This code will convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day
    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: {}".format(
        str(df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("Most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("Most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common start station: {} ".format(
        df['Start Station'].mode().values[0])
    )

    # TO DO: display most commonly used end station
    print("Most common end station: {}".format(
        df['End Station'].mode().values[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['comboroutes'] = df['Start Station']+ " " + df['End Station']
    print("Most common start and end station combination is: {}".format(
        df['comboroutes'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['TotalTrip'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print("Total travel time is: {}".format(
        str(df['TotalTrip'].sum()))
    )

    # TO DO: display mean travel time
    print("Average travel time is: {}".format(
        str(df['TotalTrip'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # Display counts of user types
    print("Here are the counts of various user types:")
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth

    if city != 'washington':
        # Display counts of gender
        print("Here are the counts of gender:")
        print(df['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        print("Earliest birth year is: {}".format(
            str(int(df['Birth Year'].min())))
        )
        print("Latest birth year: {}".format(
            str(int(df['Birth Year'].max())))
        )
        print("Most common birth year: {}".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    if city == 'washington':
        # No data
        print("No additional demographic information for Washington")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
