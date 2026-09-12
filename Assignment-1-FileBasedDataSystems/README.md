# Assignment 1: File Based Data Systems

## Overview

This project explores a structured CSV dataset using Python and pandas.  
The analysis focuses on data inspection, filtering, counting, and applying multiple conditions to answer questions about squirrel sightings in Central Park.

---

## Dataset

**Dataset:** 2018 Central Park Squirrel Census - Squirrel Data  
**Source:** NYC Open Data  
**Format:** CSV  
**Columns:** 31  

Each row represents one recorded squirrel sighting. The dataset contains information such as:

- Age
- Primary Fur Color
- Location
- Observation Shift
- Behavior
- Geographic coordinates

### Dataset Source

[2018 Central Park Squirrel Census - Squirrel Data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

---

## Why I Chose This Dataset

I chose this dataset because it contains structured information that can be explored clearly using filtering and counting operations.

The dataset includes categorical variables such as age, primary fur color, and location, which make it possible to ask meaningful questions about patterns in recorded squirrel sightings.

I also chose this dataset because each row represents an individual observation. This makes it easy to understand how rows, columns, and categorical values work together in a file-based data system.

The dataset is large enough to support useful comparisons while still being straightforward to analyze using Python and pandas.

---

## Project Files

```text
Assignment-1-FileBasedDataSystems/
│
├── analysis.py
├── README.md
└── squirrel_data.csv
```

| File | Description |
|---|---|
| `analysis.py` | Python program used to inspect and analyze the dataset |
| `squirrel_data.csv` | CSV dataset downloaded from NYC Open Data |
| `README.md` | Explanation of the dataset, questions, results, and limitations |

---

## Required Data Inspection

The Python program performs all required data inspection tasks:

1. Prints the first 2 rows
2. Prints the first row
3. Prints rows 10–19
4. Prints all column names
5. Prints the first 10 values of one column
6. Prints the first 10 rows of three selected columns
7. Answers three questions about the dataset

---

## Results Summary

| Question | Result |
|---|---|
| How many squirrels are adults? | **2,568** |
| Which primary fur color appears most frequently? | **Gray — 2,473 sightings** |
| How many squirrels are both adult and gray? | **2,125** |

---

# Data Questions

## Question 1: Adult Squirrels

### Question

**How many squirrels in the dataset are adults?**

### Python Code

```python
adult_squirrels = df[
    df["Age"] == "Adult"
]

adult_count = len(adult_squirrels)
```

### Output

```text
Answer: 2568
```

The dataset contains **2,568 adult squirrel sightings**.

### Why the Data Supports This Question

The dataset contains an `Age` column that records the age category associated with each squirrel sighting.

Because each row represents one recorded sighting, the dataset can be filtered to retain only rows where `Age` is equal to `Adult`.

The number of remaining rows can then be counted to determine how many adult squirrel sightings appear in the dataset.

---

## Question 2: Most Common Fur Color

### Question

**Which primary fur color appears most frequently in the dataset?**

### Python Code

```python
fur_color_counts = df[
    "Primary Fur Color"
].value_counts()

most_common_color = fur_color_counts.idxmax()

most_common_color_count = fur_color_counts.max()
```

### Output

```text
Answer: Gray
Number of sightings: 2473
```

The most frequently recorded primary fur color is **Gray**, with **2,473 sightings**.

### Why the Data Supports This Question

The dataset contains a categorical column named `Primary Fur Color`.

Because this value is recorded for individual squirrel sightings, Python can count how many times each fur-color category appears.

The resulting counts can then be compared to determine which primary fur color occurs most frequently.

---

## Question 3: Adult Gray Squirrels

### Question

**How many adult squirrels with gray primary fur color were observed?**

### Python Code

```python
adult_gray_squirrels = df[
    (df["Age"] == "Adult")
    &
    (df["Primary Fur Color"] == "Gray")
]

adult_gray_count = len(
    adult_gray_squirrels
)
```

### Output

```text
Answer: 2125
```

There are **2,125 squirrel sightings** that satisfy both conditions:

- `Age` is `Adult`
- `Primary Fur Color` is `Gray`

### Why the Data Supports This Question

The dataset stores age and primary fur color in separate columns.

This structure allows the dataset to be filtered using two conditions simultaneously. A row must contain both `Adult` in the `Age` column and `Gray` in the `Primary Fur Color` column to satisfy the filter.

The resulting rows can then be counted.

This question demonstrates how multiple conditions can be applied to structured data at the same time.

---

# What the Data Cannot Answer

One question I would like to answer is whether adult gray squirrels actually make up a larger proportion of the entire squirrel population in Central Park than squirrels belonging to other age or fur-color categories.

The dataset cannot fully answer this question because it contains recorded squirrel sightings rather than a guaranteed complete count of every squirrel living in Central Park. Some squirrels may not have been observed, while others may have been more likely to be detected because of their location, behavior, visibility, or the amount of observation effort in a particular area.

Additional information would be needed to estimate the true squirrel population. Useful information could include observation time in each area, the number of observers, detection probability, whether the same squirrel could have been observed more than once, and independent estimates of the total squirrel population.

Therefore, it would be misleading to assume that the proportions of squirrel sightings in this dataset are exactly the same as the proportions in the true Central Park squirrel population. The dataset can describe the recorded observations, but stronger population-level conclusions would require additional sampling information.

---

## Implementation

This project uses **Python** and **pandas**.

The dataset is loaded with:

```python
import pandas as pd

df = pd.read_csv("squirrel_data.csv")
```

The analysis demonstrates:

- CSV data loading
- Row inspection
- Column inspection
- Column selection
- Filtering
- Counting
- Categorical value analysis
- Two-condition filtering

---

## How to Run

Make sure Python and pandas are installed.

Install pandas if necessary:

```bash
pip install pandas
```

Run the analysis:

```bash
python analysis.py
```

The program will print the required inspection results followed by the answers to the three data questions.

---

## Dataset Source

**NYC Open Data**  
**2018 Central Park Squirrel Census - Squirrel Data**

https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw


















(.venv) PS C:\Users\zkz05\OneDrive\Desktop\CSCI-UA 60 HW FOR ALL\Assignment-1-FileBasedDataSystems> python analysis.py
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