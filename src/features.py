import pandas as pd
import streamlit as st



def prepare_data(test_file):
    """

    Cleans data and prepare data for modeling.


    Args:

        path: Path to the csv file.


    Returns:

        A tuple containing the features DataFrame and the target variable.
    """
    
    test_file = test_file
   
    features = test_file.columns

    df = pd.read_csv("data/ransomware_dataset.csv") # training file
    df['family'] = df['family'].replace(['G'], 0)
    df['family'] = df['family'].replace(['E'], 1)
    df['family'] = df['family'].replace(['L'], 2)

    target = df['family']

    # use the same number of features as uploaded file

    features = df[features]
   
    return features, target
