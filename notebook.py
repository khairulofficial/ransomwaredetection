import streamlit as st

# for data manipulation
import numpy as np
import pandas as pd


# for machine learning
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,mean_squared_error, r2_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

# instructions
st.title("Ransomware Detection Web App")
st.write("""
1. Click "Browse File" to upload the generated csv file.
2. Select machine learning model. If unsure, please consult admin or use recommended model.
3. Click "Predict"
""")

# file upload
sample = st.sidebar.file_uploader(label="Upload Generated CSV File", type="csv", accept_multiple_files=False)

# display result
if sample is not None:
    # read uploaded file into df and get the columns

    df2 = pd.read_csv(sample)

    

    try:
        features = df2.columns

        # read file containing past data
        df = pd.read_csv("ransomware_dataset.csv")

        df['family'] = df['family'].replace(['G'], 'Goodware')
        df['family'] = df['family'].replace(['E'], 'Encryptor Ransomware')
        df['family'] = df['family'].replace(['L'], 'Locker Ransomware')

        y = df['family']
        # use the same number of features as uploaded file
        X = df[features]


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

        # model selection button
        model = st.sidebar.selectbox(label="Select Machine Learning model", options=['Random Forest (Recommended)','Support Vector Machine','Logistic Regression','Naive Bayes','K-Nearest-Neighbour','Gradient Boosted Trees','Neural Network'])

        if model == "Support Vector Machine":
            clf = SVC(kernel='rbf', random_state=1)

        elif model == "Logistic Regression":
            clf = LogisticRegression(max_iter = 1000, random_state=0, solver="saga")

        elif model == "Naive Bayes":
            clf = GaussianNB()
            
        elif model == "K-Nearest-Neighbour":
            clf = KNeighborsClassifier()

        elif model == "Gradient Boosted Trees":
            clf = GradientBoostingClassifier(n_estimators=100)
            
        elif model == "Random Forest (Recommended)":
            clf = RandomForestClassifier(n_estimators=100)
            
        elif model == "Neural Network":
            clf = MLPClassifier(hidden_layer_sizes=(100,100,100),activation='relu')
            
        

        # upon clicking predict
        if st.sidebar.button('Predict'):
            clf.fit(X_train, y_train)
            family = clf.predict(df2)

            # display prediction
            st.header(f'Result: This file is predicted to be a {family[0]}')
            if family[0] == "Locker Ransomware" or family[0] == "Encryptor Ransomware":
                # display further instructions
                st.write('WARNING: Please delete the file if you have accidentally download it on any device and inform your admin')

            # model and file details
            st.write(f"Model: {model}")
            cvscore = cross_val_score(clf,X,y,cv=10).mean()
            st.write("Accuracy: ",f"{cvscore:.2%}")
            # st.write('File details:')
            # st.write(df2)
    
    # handle invalid uploads
    except:
        st.warning("Invalid file. Please upload a valid file.")