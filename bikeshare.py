import time
import pandas as pd
import numpy as np

"""  Python dictionary for the cities and their csv files  """
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
    # getting user input for city (chicago, new york city, washington). 
    city = input('Please enter the city of your choice (chicago or new york city or washington): ')
    #converting the input to lower case
    city = city.lower()
    #handling invalid inputs
    while city not in ('chicago','new york city', 'washington') :
        print('I did\'t capture that')
        city = input('Please enter the city of your choice (chicago or new york city or washington): ')
        city = city.lower()
    
    # getting user input for month (all, january, february, ... , june)
    month = input('Please enter the month (january ..... june) or all to use all the months: ')
    #converting the input into lower case
    month = month.lower()
    #handling invalid inputs
    while month not in ('all','january','february','march','april','may','june'):
        print('I did\'t capture that')
        month = input('Please enter the month (january ... june) or all to use all the months: ')
        month = month.lower()


    # getting user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day of the week (all, monday ... sunday): ')
    #converting the day input into lower case
    day = day.lower()
    #handling invalid inputs
    while day not in ('all','monday','tuesday','wednesday','thursday','friday','sunday'):
        print('I did\'t capture that')
        day = input('Please enter the day of the week (all, monday ... sunday): ')
        day = day.lower()


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    #print(df['day_of_week'].head())

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        df = df[df['day_of_week'] == days.index(day)]
        #df = df['day_of_week']


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month_index = df['month'].value_counts()[:1].index.tolist()[0]
    print('{} is the most common month.\n'.format(month_list[month_index-1]))


    # display the most common day of week
    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day_index = df['day_of_week'].value_counts()[:1].index.tolist()[0]
    print('{} is the most common day of the week.\n'.format(day_list[day_index]))

    # extract hour from Start Time to create the hour column
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    # display the most common start hour
    print('{} is the most common start hour.\n'.format(df['hour'].value_counts()[:1].index.tolist()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('{} is the most commonly used start station.\n'.format(df['Start Station'].value_counts()[:1].index.tolist()[0]))

    # display most commonly used end station
    print('{} is the most common end station used.\n'.format(df['End Station'].value_counts()[:1].index.tolist()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['freq_comb'] = df['Start Station'] + ' and ' + df['End Station']
    print('{} is most frequent combination'.format(df['freq_comb'].value_counts()[:1].index.tolist()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_seconds = df['Trip Duration'].sum()
    # travel_minute
    print('the total travel time is {}s.\n'.format(travel_seconds))

    # TO DO: display mean travel time
    print('the mean travel time is {}s.\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('displaying the user types {}.\n'.format(df['User Type'].value_counts()))

    try:
        # Display counts of gender
        print ('displaying gender counts: {}.\n'.format(df['Gender'].value_counts()))

    except KeyError :
        print('missing \'Gender\' column in the data.\n')
    try:
        # Display earliest, most recent, and most common year of birth
        print('{} is the earliest year of birth.\n'.format(int(df['Birth Year'].min())))
        print('{} is the recent year of birth.\n'.format(int(df['Birth Year'].max())))
        print('{} is the most common year of birth.\n'.format(int(df['Birth Year'].value_counts().index.tolist()[0])))
    except KeyError:
        print('missing \'Birth Year\' column in the data.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#def raw_data(df):
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data_response = input('\n Would you like to view raw data? Enter yes or no.')
        count = 0
        while raw_data_response.lower() == 'yes':
            print(df.iloc[count:(5+count)])
            count += 5
            raw_data_response = input('\n Would you like to view the next 5 rows of raw data? Enter yes or no.')
            #raw_data_response = raw_data_response.lower()
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
