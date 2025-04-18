#!/usr/bin/env python
# coding: utf-8
import pandas as pd

# function that can read the header of the object type: <class '_csv.reader'>
def read_header(dataset):
    headers = next(dataset)
    print("Headers: ", headers)
    
# function that can print the first X rows of the dataset:
def print_X_rows(X, data_set):
    print("First {X} rows: ".format(X=X))
    print(data_set.head(X))

# function that print the unique values (or arguments) for non-numeric (categorical) columns from the dataset, using pandas.
def all_unique_categorical_values(df):
    # I loop through each column to identify non-numeric columns (not int nor float)
    for column in df.columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            print(f"Unique values in '{column}':")
            print(df[column].unique(),"\n")


# Checking if there are missing values in the dataset:
def if_missing_data(df):
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values)


# In which row are the missing values?
def where_the_missing_data(df):
    print(df[df.isnull().any(axis=1)])
    if df.isnull().sum().sum() == 0:
        print("Good News! There is no missing data!")


#get_ipython().system('jupyter nbconvert --to script data_utils.ipynb')



