import pandas as pd


# ============================================================
# Assignment 1: File Based Data Systems
# Dataset: 2018 Central Park Squirrel Census
# Source: NYC Open Data
# ============================================================


# ------------------------------------------------------------
# LOAD THE DATASET
# ------------------------------------------------------------

# Read the CSV file into a pandas DataFrame.
# A DataFrame stores the CSV data in rows and columns.
df = pd.read_csv("squirrel_data.csv")


# ============================================================
# REQUIRED DATA INSPECTION TASKS
# ============================================================


# ------------------------------------------------------------
# Task 1
# Print the first 2 rows of the dataset.
# ------------------------------------------------------------

print("=" * 60)
print("TASK 1: FIRST 2 ROWS")
print("=" * 60)

print(df.head(2))

print()


# ------------------------------------------------------------
# Task 2
# Print the first row of the dataset.
# ------------------------------------------------------------

print("=" * 60)
print("TASK 2: FIRST ROW")
print("=" * 60)

print(df.iloc[0])

print()


# ------------------------------------------------------------
# Task 3
# Print rows 10 through 19.
#
# Python uses zero-based indexing.
# iloc[10:20] includes row positions 10 through 19.
# ------------------------------------------------------------

print("=" * 60)
print("TASK 3: ROWS 10-19")
print("=" * 60)

print(df.iloc[10:20])

print()


# ------------------------------------------------------------
# Task 4
# Print the column names.
# ------------------------------------------------------------

print("=" * 60)
print("TASK 4: COLUMN NAMES")
print("=" * 60)

print(df.columns.tolist())

print()


# ------------------------------------------------------------
# Task 5
# Print the first 10 values from one column.
#
# We use the Age column because it contains categorical data.
# ------------------------------------------------------------

print("=" * 60)
print("TASK 5: FIRST 10 VALUES OF AGE")
print("=" * 60)

print(df["Age"].head(10))

print()


# ------------------------------------------------------------
# Task 6
# Print the first 10 rows of three columns.
#
# These columns represent three different characteristics
# recorded for each squirrel sighting.
# ------------------------------------------------------------

print("=" * 60)
print("TASK 6: FIRST 10 ROWS OF THREE COLUMNS")
print("=" * 60)

print(
    df[
        [
            "Age",
            "Primary Fur Color",
            "Location"
        ]
    ].head(10)
)

print()


# ============================================================
# DATA QUESTION 1
# ============================================================

# Question:
# How many squirrels in the dataset are adults?
#
# This uses filtering and counting.
#
# First, filter the DataFrame so that only rows where
# Age equals "Adult" remain.
# Then count how many rows are in the filtered DataFrame.

print("=" * 60)
print("QUESTION 1")
print("=" * 60)

adult_squirrels = df[
    df["Age"] == "Adult"
]

adult_count = len(adult_squirrels)

print("How many squirrels in the dataset are adults?")
print("Answer:", adult_count)

print()


# ============================================================
# DATA QUESTION 2
# ============================================================

# Question:
# Which primary fur color appears most frequently?
#
# value_counts() counts how many times each category appears.
#
# idxmax() returns the category with the largest count.
#
# max() returns that largest count.

print("=" * 60)
print("QUESTION 2")
print("=" * 60)

fur_color_counts = df[
    "Primary Fur Color"
].value_counts()

most_common_color = fur_color_counts.idxmax()

most_common_color_count = fur_color_counts.max()

print("Which primary fur color appears most frequently?")
print("Answer:", most_common_color)
print(
    "Number of sightings:",
    most_common_color_count
)

print()


# ============================================================
# DATA QUESTION 3
# ============================================================

# Question:
# How many adult squirrels with gray primary fur color
# were observed?
#
# This question intentionally uses TWO filtering conditions:
#
# Condition 1:
# Age must equal "Adult"
#
# Condition 2:
# Primary Fur Color must equal "Gray"
#
# The & operator means BOTH conditions must be true.

print("=" * 60)
print("QUESTION 3")
print("=" * 60)

adult_gray_squirrels = df[
    (df["Age"] == "Adult")
    &
    (df["Primary Fur Color"] == "Gray")
]

adult_gray_count = len(
    adult_gray_squirrels
)

print(
    "How many adult squirrels with gray "
    "primary fur color were observed?"
)

print(
    "Answer:",
    adult_gray_count
)

print()


# ============================================================
# END OF ANALYSIS
# ============================================================

print("=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)