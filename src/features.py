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

    url = 'https://raw.githubusercontent.com/Juan-Herrera-Silva/Paper-SENSORS/main/Annex%20A%20-%20Dataset%20with%2050%20chosen%20features.csv'
    df = pd.read_csv(url) # training file
    df['family'] = df['family'].replace(['G'], 0)
    df['family'] = df['family'].replace(['E'], 1)
    df['family'] = df['family'].replace(['L'], 2)

    target = df['family']

    # use the same number of features as uploaded file

    features = df[features]
   
    return features, target
