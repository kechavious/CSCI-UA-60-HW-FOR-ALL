PS C:\Users\zkz05\OneDrive\Desktop\Assignment-1-FileBasedDataSystems> python analysis.py
============================================================
TASK 1: FIRST 2 ROWS
============================================================
           X          Y Unique Squirrel ID Hectare Shift      Date  ...  Tail twitches Approaches Indifferent Runs from Other Interactions                                    Lat/Long
0 -73.956134  40.794082     37F-PM-1014-03     37F    PM  10142018  ...          False      False       False     False                NaN  POINT (-73.9561344937861 40.7940823884086)
1 -73.968857  40.783783     21B-AM-1019-04     21B    AM  10192018  ...          False      False       False     False                NaN  POINT (-73.9688574691102 40.7837825208444)

[2 rows x 31 columns]

============================================================
TASK 2: FIRST ROW
============================================================
X                                                                             -73.956134
Y                                                                              40.794082
Unique Squirrel ID                                                        37F-PM-1014-03
Hectare                                                                              37F
Shift                                                                                 PM
Date                                                                            10142018
Hectare Squirrel Number                                                                3
Age                                                                                  NaN
Primary Fur Color                                                                    NaN
Highlight Fur Color                                                                  NaN
Combination of Primary and Highlight Color                                             +
Color notes                                                                          NaN
Location                                                                             NaN
Above Ground Sighter Measurement                                                     NaN
Specific Location                                                                    NaN
Running                                                                            False
Chasing                                                                            False
Climbing                                                                           False
Eating                                                                             False
Foraging                                                                           False
Other Activities                                                                     NaN
Kuks                                                                               False
Quaas                                                                              False
Moans                                                                              False
Tail flags                                                                         False
Tail twitches                                                                      False
Approaches                                                                         False
Indifferent                                                                        False
Runs from                                                                          False
Other Interactions                                                                   NaN
Lat/Long                                      POINT (-73.9561344937861 40.7940823884086)
Name: 0, dtype: object

============================================================
TASK 3: ROWS 10-19
============================================================
            X          Y Unique Squirrel ID Hectare Shift      Date  ...  Tail twitches Approaches Indifferent Runs from Other Interactions                                    Lat/Long
10 -73.969506  40.782351     20B-PM-1013-05     20B    PM  10132018  ...          False      False        True     False                NaN  POINT (-73.9695063535333 40.7823507678183)
11 -73.964003  40.782031     22F-PM-1014-06     22F    PM  10142018  ...           True      False        True     False                NaN  POINT (-73.9640032826529 40.7820309825448)
12 -73.953217  40.791967     36I-PM-1007-01     36I    PM  10072018  ...          False      False        True     False                NaN  POINT (-73.9532170504865 40.7919669739962)
13 -73.976860  40.770280      5C-PM-1010-09     05C    PM  10102018  ...          False      False       False     False                NaN  POINT (-73.9768603630674 40.7702795904962)
14 -73.970611  40.769812      7H-AM-1006-05     07H    AM  10062018  ...          False      False        True     False                NaN  POINT (-73.9706105896967 40.7698124821507)
15 -73.970378  40.778753     16C-PM-1018-03     16C    PM  10182018  ...          False      False        True     False                NaN  POINT (-73.9703781726172 40.7787526130321)
16 -73.970393  40.776503     14E-AM-1008-23     14E    AM  10082018  ...          False      False        True     False                NaN  POINT (-73.9703925210471 40.7765032004992)
17 -73.963818  40.792417     32A-PM-1013-03     32A    PM  10132018  ...          False      False        True     False                NaN  POINT (-73.9638179439747 40.7924173263904)
18 -73.958407  40.791381     33F-AM-1008-01     33F    AM  10082018  ...          False      False        True     False                NaN  POINT (-73.9584070974734 40.7913812490557)
19 -73.967113  40.778486     17F-AM-1007-07     17F    AM  10072018  ...          False      False        True     False                NaN  POINT (-73.9671130680114 40.7784859700171)

[10 rows x 31 columns]

============================================================
TASK 4: COLUMN NAMES
============================================================
['X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date', 'Hectare Squirrel Number', 'Age', 'Primary Fur Color', 'Highlight Fur Color', 'Combination of Primary and Highlight Color', 'Color notes', 'Location', 'Above Ground Sighter Measurement', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from', 'Other Interactions', 'Lat/Long']

============================================================
TASK 5: FIRST 10 VALUES OF AGE
============================================================
0      NaN
1      NaN
2      NaN
3    Adult
4    Adult
5    Adult
6    Adult
7    Adult
8    Adult
9    Adult
Name: Age, dtype: str

============================================================
TASK 6: FIRST 10 ROWS OF THREE COLUMNS
============================================================
     Age Primary Fur Color      Location
0    NaN               NaN           NaN
1    NaN               NaN           NaN
2    NaN              Gray  Above Ground
3  Adult              Gray           NaN
4  Adult              Gray  Above Ground
5  Adult          Cinnamon           NaN
6  Adult              Gray  Ground Plane
7  Adult              Gray  Ground Plane
8  Adult              Gray  Ground Plane
9  Adult              Gray  Above Ground

============================================================
QUESTION 1
============================================================
How many squirrels in the dataset are adults?
Answer: 2568

============================================================
QUESTION 2
============================================================
Which primary fur color appears most frequently?
Answer: Gray
Number of sightings: 2473

============================================================
QUESTION 3
============================================================
How many adult squirrels with gray primary fur color were observed?
Answer: 2125

============================================================
ANALYSIS COMPLETE
============================================================









# Assignment 1: File Based Data Systems

## Dataset

For this assignment, I used the **2018 Central Park Squirrel Census - Squirrel Data** dataset from NYC Open Data.

The dataset contains individual squirrel sightings collected during the 2018 Central Park Squirrel Census. Each row represents a recorded squirrel sighting, while the columns describe characteristics associated with that sighting, including age, primary fur color, location, behavior, and other observations.

Dataset source:

https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw


## Why I Chose This Dataset

I chose this dataset because it contains structured information that can be explored clearly using filtering and counting operations.

The dataset contains categorical variables such as age, primary fur color, and location. These variables make it possible to ask meaningful questions about patterns in recorded squirrel sightings.

I also chose this dataset because each row represents an individual observation. This makes it easy to understand how rows, columns, and categories work together in a file-based data system.

The dataset is also large enough to make comparisons meaningful while still being straightforward to analyze using Python and pandas.


# Data Questions


## Question 1

### Question

How many squirrels in the dataset are adults?

### Python Code

```python
adult_squirrels = df[
    df["Age"] == "Adult"
]

adult_count = len(adult_squirrels)
Output

2568

The dataset contains 2,568 adult squirrel sightings.

Why the Data Supports This Question

The dataset contains an Age column that records the age category associated with individual squirrel sightings.

Because each row represents one recorded squirrel sighting, the dataset can be filtered to retain only rows where the Age column contains Adult.

The number of remaining rows can then be counted to determine how many adult squirrel sightings appear in the dataset.

Question 2
Question

Which primary fur color appears most frequently in the dataset?

Python Code
fur_color_counts = df[
    "Primary Fur Color"
].value_counts()

most_common_color = fur_color_counts.idxmax()

most_common_color_count = fur_color_counts.max()
Output

Gray

Number of sightings: 2473

The most frequently recorded primary fur color is Gray, with 2,473 sightings.

Why the Data Supports This Question

The dataset contains a categorical column named Primary Fur Color.

Because this value is recorded for individual squirrel sightings, Python can count how many times each fur-color category occurs.

The resulting counts can then be compared to determine which primary fur color appears most frequently in the dataset.

Question 3
Question

How many adult squirrels with gray primary fur color were observed?

Python Code
adult_gray_squirrels = df[
    (df["Age"] == "Adult")
    &
    (df["Primary Fur Color"] == "Gray")
]

adult_gray_count = len(
    adult_gray_squirrels
)
Output

2125

There are 2,125 recorded squirrel sightings that are both adult and have gray primary fur color.

Why the Data Supports This Question

The dataset records age and primary fur color in separate columns.

This structure makes it possible to filter the dataset using both variables simultaneously.

A row must have Adult in the Age column and Gray in the Primary Fur Color column to satisfy the conditions.

The resulting rows can then be counted.

This question demonstrates how multiple conditions can be applied to structured data at the same time.

What the Data Cannot Answer

One question I would like to answer is whether adult gray squirrels truly make up a larger proportion of the entire squirrel population in Central Park than squirrels belonging to other age or fur-color categories.

The dataset cannot fully answer this question because it contains recorded squirrel sightings rather than a guaranteed complete count of every squirrel living in Central Park. Some squirrels may not have been observed, while others may have been more likely to be detected because of their location, behavior, visibility, or the amount of observation effort in a particular part of the park.

Additional information would therefore be needed to estimate the true squirrel population. Useful information could include the amount of observation time in each area, the number of observers, detection probability, whether the same squirrel could have been observed more than once, and independent estimates of the total squirrel population.

It would therefore be misleading to assume that the proportions of squirrel sightings in this dataset are exactly the same as the proportions in the true Central Park squirrel population. The dataset can accurately describe the recorded observations, but stronger population-level conclusions would require additional sampling information.

Files

This repository contains:

analysis.py — Python code used to inspect and analyze the dataset.
squirrel_data.csv — CSV dataset downloaded from NYC Open Data.
README.md — Dataset explanation, data questions, and reflection.
Implementation

This assignment uses Python with the pandas library.

The CSV file is loaded using:

df = pd.read_csv("squirrel_data.csv")

The analysis includes:

loading structured CSV data
inspecting rows and columns
selecting specific columns
filtering rows
counting filtered observations
counting categorical values
filtering with multiple conditions
Dataset Source

NYC Open Data

2018 Central Park Squirrel Census - Squirrel Data

https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw