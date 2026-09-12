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