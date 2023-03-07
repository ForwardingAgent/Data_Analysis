import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    cvs_url = 'https://replit.com/@NikolayPodkopae/boilerplate-demographic-data-analyzer'
    df = pd.read_csv(cvs_url)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df['race'].value_counts()
    all_race = list(df['race'].value_counts())
    race_count = all_race

    # What is the average age of men?
    filter_Male = df['sex'] == 'Male'  # фильтр по Male
    df_Male = df.loc[filter_Male]  # df с фильтром
    df_Male['age'].count()  # общее кол-во rows по Male
    df_Male['age'].sum()  #  сумма всех age по Male
    average_age = df_Male['age'].sum() / df_Male['age'].count()
    average_age_men = float('%.1f' % average_age)

    # What is the percentage of people who have a Bachelor's degree?
    all_edu_value = df['education'].value_counts()  # общее кол-во по степеням (возьмем кол-во (Bachelors) по индексу [2])
    df['education'].count()  # общее число всех степеней
    bachelors_percent = (all_edu_value[2] * 100) / df['education'].count() #     процент Bachelors в общем количестве
    percentage_bachelors = float('%.1f' % bachelors_percent)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE